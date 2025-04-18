#!/usr/bin/env python3

import enum
import re
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple, Union

import click
import numpy as np
import pandas as pd
from loguru import logger
from pydantic import BaseModel
from rich import print

# Configure logger
logger.add("whatsapp_analyzer.log", rotation="1 MB")


class Labels(str, enum.Enum):
    """Enumeration for single-label text classification."""

    MALE = "male"
    FEMALE = "female"
    UNDECIDED = "undecided"


class SinglePrediction(BaseModel):
    """Class for a single class label prediction."""

    class_label: Labels
    class_probability: float


def parse_chat_line(line: str) -> Optional[Tuple[datetime, str, str]]:
    """Parse a single line from a WhatsApp chat export.

    Args:
        line: A line from the chat export

    Returns:
        Tuple of (datetime, sender, message) if successful, None otherwise
    """
    patterns = [
        r"\[(.*?)\] (.*?): (.*)",  # Default pattern
        r"\[(.*?)\] ~\u202f(.*?): (.*)",  # Pattern with ~ and non-breaking space
        r"(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*)",  # Pattern for system messages
    ]

    for pattern in patterns:
        match = re.match(pattern, line)
        if match:
            if len(match.groups()) == 3:
                date_time_str, sender, message = match.groups()
            elif len(match.groups()) == 2:
                date_time_str, message = match.groups()
                sender = "System"
            try:
                date_time = datetime.strptime(date_time_str, "%Y-%m-%d, %H:%M:%S")
            except ValueError:
                try:
                    date_time = datetime.strptime(
                        date_time_str, "%d/%m/%y, %I:%M:%S\u202f%p"
                    )
                except ValueError:
                    try:
                        date_time = datetime.strptime(date_time_str, "%d/%m/%Y, %H:%M")
                    except ValueError:
                        continue
            return date_time, sender.strip(), message.strip()
    return None


def parse_chat(file_path: Union[str, Path]) -> pd.DataFrame:
    """Parse a WhatsApp chat log into a DataFrame.

    Args:
        file_path: Path to the chat log file

    Returns:
        DataFrame containing the parsed chat with columns 'Sender', 'Datetime', 'Message'
    """
    parsed_data = []
    with open(file_path, "r") as file:
        for _, line in enumerate(file):
            parsed_line = parse_chat_line(line)
            if parsed_line:
                parsed_data.append(parsed_line)

    # Creating a DataFrame
    df = pd.DataFrame(parsed_data, columns=["Datetime", "Sender", "Message"])
    return df


def cleanup(df: pd.DataFrame) -> pd.DataFrame:
    """Clean up the DataFrame by removing system messages and duplicates.

    Args:
        df: DataFrame containing message data

    Returns:
        Cleaned DataFrame
    """
    df = df.drop_duplicates(subset=["Datetime", "Sender", "Message"])
    df = df.sort_values(by="Datetime")

    # Remove system messages
    system_messages = [
        "deleted this message",
        "message was deleted",
        "changed the subject to",
        "changed the group description",
        "reset this group's invite link",
        "changed this group's icon",
        "changed the subject from",
        "changed this group's settings",
    ]

    for message in system_messages:
        df = df[~df["Message"].str.contains(message)]

    logger.info(f"Cleaned DataFrame has {len(df)} messages")
    return df


def chat_to_df(
    file_path: Path,
    previous_df_path: Optional[Path] = None,
    group_name: Optional[str] = None,
) -> pd.DataFrame:
    """Convert a WhatsApp chat export to a DataFrame.

    Args:
        file_path: Path to the chat export file
        previous_df_path: Optional path to a previous DataFrame to merge with
        group_name: Optional name of the group to add as a column

    Returns:
        DataFrame containing the chat data
    """
    file_path = Path(file_path)
    assert file_path.exists(), f"File not found: {file_path}"

    df = parse_chat(file_path=file_path)
    df = cleanup(df)

    if previous_df_path:
        previous_df = pd.read_csv(previous_df_path, sep="|")
        previous_df["Datetime"] = pd.to_datetime(previous_df["Datetime"])
        df = pd.concat([df, previous_df], ignore_index=True)
        df = cleanup(df)

    if group_name:
        logger.info(f"Adding group name {group_name} to the chat")
        df["Group"] = group_name
    return df


class WhatsAppGroupAnalysis:
    """Class for analyzing WhatsApp group chat data."""

    def __init__(self, df: pd.DataFrame) -> None:
        """Initialize with a DataFrame containing message data.

        Args:
            df: DataFrame with 'Datetime' and 'Sender' columns
        """
        self.df = df
        # Convert the 'Datetime' column to a datetime object
        self.df["Datetime"] = pd.to_datetime(self.df["Datetime"])
        logger.info(f"Initialized WhatsAppGroupAnalysis with {len(df)} messages")

    def get_current_users(self) -> Tuple[pd.DataFrame, int]:
        """Get the current users in the group.

        Returns:
            Tuple of (DataFrame with current users, count of current users)
        """
        # Identifying patterns for joining, being added, and leaving or being removed
        joining_pattern = self.df["Message"].str.contains(
            "joined using this group|added", case=False, na=False
        )
        leaving_pattern = self.df["Message"].str.contains(
            "left|removed", case=False, na=False
        )
        # Extracting users who have joined or been added
        joined_users = self.df[joining_pattern]["Sender"].unique()
        # Extracting users who have left or been removed
        left_users = self.df[leaving_pattern]["Sender"].unique()
        # Finding current users by excluding those who have left or been removed
        current_users = [user for user in joined_users if user not in left_users]
        # Creating a DataFrame with current users
        current_users_df = pd.DataFrame(current_users, columns=["User"])
        current_users_count = len(current_users)
        logger.info(f"Found {current_users_count} current users")
        return current_users_df, current_users_count

    def get_message_count_in_window(self, window_days: int = 60) -> pd.DataFrame:
        """Get the message count for each user in a time window.

        Args:
            window_days: Number of days to look back, defaults to 60

        Returns:
            DataFrame with message counts per user in the window
        """
        # Get the maximum date in the DataFrame
        max_date = self.df["Datetime"].max()
        # Calculate the start date based on the window_days parameter
        start_date = max_date - pd.Timedelta(days=window_days)
        # Filter messages within the given window
        messages_in_window = self.df[self.df["Datetime"] > start_date]
        # Count messages per user
        message_count_in_window = (
            messages_in_window["Sender"].value_counts().reset_index()
        )
        message_count_in_window.columns = ["User", "Message_Count_In_Window"]
        logger.info(
            f"Message counts calculated for {len(message_count_in_window)} users in {window_days} day window"
        )
        return message_count_in_window

    def get_inactive_users(self, exclude_contacts: bool = False) -> pd.DataFrame:
        """Get users who have been inactive.

        Args:
            exclude_contacts: Whether to exclude contacts (users with names starting with '~'), defaults to False

        Returns:
            DataFrame with inactive users and their statistics
        """
        # Get users with zero messages
        users_with_zero_messages = self.get_users_with_zero_messages()
        # Filter users whose usernames start with a tilde ("~")
        if exclude_contacts:
            inactive_users = users_with_zero_messages[
                users_with_zero_messages["User"].str.startswith("~")
            ]
        else:
            inactive_users = users_with_zero_messages
        # Get users with joining date
        users_with_joining_date = self.get_users_with_joining_date()
        # Merge inactive users with joining dates
        inactive_users_with_joining_date = pd.merge(
            inactive_users, users_with_joining_date, on="User", how="left"
        )
        # Get the cutoff date for the last 60 days
        max_date = self.df["Datetime"].max()
        cutoff_date = max_date - pd.Timedelta(days=60)
        # Filter users who joined more than 60 days ago
        filtered_inactive_users = inactive_users_with_joining_date[
            inactive_users_with_joining_date["Joining_Date"] < cutoff_date
        ]
        # Count total messages sent by each user since the beginning
        total_message_count = self.df["Sender"].value_counts().reset_index()
        total_message_count.columns = ["User", "Total_Messages_Sent"]
        # Merge with total messages sent
        filtered_inactive_users_with_messages = pd.merge(
            filtered_inactive_users, total_message_count, on="User", how="left"
        ).fillna(0)
        # Find the most recent message date for each user
        most_recent_message_date = (
            self.df.groupby("Sender")["Datetime"].max().reset_index()
        )
        most_recent_message_date.columns = ["User", "Most_Recent_Message_Date"]
        # Merge with the most recent message date
        filtered_inactive_users_with_recent_message = pd.merge(
            filtered_inactive_users_with_messages,
            most_recent_message_date,
            on="User",
            how="left",
        )
        logger.info(
            f"Found {len(filtered_inactive_users_with_recent_message)} inactive users"
        )
        return filtered_inactive_users_with_recent_message

    def get_users_with_zero_messages(self) -> pd.DataFrame:
        """Get users who have sent zero messages in the last 60 days.

        Returns:
            DataFrame with users who have sent zero messages
        """
        # Get current users
        current_users_df, _ = self.get_current_users()
        # Get message count in the last 60 days
        message_count_in_window = self.get_message_count_in_window(60)
        # Merge current users with message count
        users_with_messages = pd.merge(
            current_users_df, message_count_in_window, on="User", how="left"
        ).fillna(0)
        # Filter users with 0 messages
        users_with_zero_messages = users_with_messages[
            users_with_messages["Message_Count_In_Window"] == 0
        ]
        logger.info(f"Found {len(users_with_zero_messages)} users with zero messages")
        return users_with_zero_messages

    def get_users_with_joining_date(self) -> pd.DataFrame:
        """Get the joining date for each user.

        Returns:
            DataFrame with user joining dates
        """
        # Identifying pattern for joining or being added
        joining_pattern = self.df["Message"].str.contains(
            "joined using this group|added", case=False, na=False
        )
        # Extracting joining dates and users
        joining_dates_df = self.df[joining_pattern][["Sender", "Datetime"]].copy()
        joining_dates_df.columns = ["User", "Joining_Date"]
        # Keep the earliest joining date for each user
        users_with_joining_date = joining_dates_df.groupby("User").min().reset_index()
        logger.info(f"Found joining dates for {len(users_with_joining_date)} users")
        return users_with_joining_date

    def calculate_activity_score(
        self,
        inactive_users_df: pd.DataFrame,
        decay_days: int = 90,
        reference_messages: int = 5,
    ) -> pd.DataFrame:
        """Calculate an exponential decay activity score for inactive users.

        Args:
            inactive_users_df: DataFrame with inactive users
            decay_days: Number of days for score to decay to zero, defaults to 90
            reference_messages: Number of messages that would give a score of 1.0, defaults to 5

        Returns:
            DataFrame with activity scores added
        """
        # Make a copy to avoid modifying the original
        df = inactive_users_df.copy()

        # Get the current date (max date in the dataset)
        current_date = self.df["Datetime"].max()

        # Calculate days since last message for each user
        df["Days_Since_Last_Message"] = (
            current_date - df["Most_Recent_Message_Date"]
        ).dt.days

        # Calculate the activity score using exponential decay
        # Score = (Total_Messages_Sent / reference_messages) * exp(-lambda * days_since_last_message)
        # where lambda = ln(2) / decay_days (half-life)
        lambda_decay = np.log(2) / decay_days

        # Calculate the base score (normalized by reference_messages)
        df["Base_Score"] = df["Total_Messages_Sent"] / reference_messages

        # Apply the exponential decay
        df["Activity_Score"] = df["Base_Score"] * np.exp(
            -lambda_decay * df["Days_Since_Last_Message"]
        )

        # Cap the score at 1.0
        df["Activity_Score"] = df["Activity_Score"].clip(upper=1.0)

        # Round the score to 3 decimal places
        df["Activity_Score"] = df["Activity_Score"].round(3)

        # Sort by activity score (lowest first)
        df = df.sort_values("Activity_Score", ascending=True)

        logger.info(f"Calculated activity scores for {len(df)} inactive users")
        return df


@click.group()
def cli():
    """WhatsApp Group Analysis Tool"""
    pass


@cli.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output", "-o", type=click.Path(path_type=Path), help="Output file path"
)
@click.option(
    "--window-days", "-w", default=60, help="Window in days to consider for inactivity"
)
@click.option(
    "--exclude-contacts/--include-contacts",
    default=False,
    help="Exclude contacts (users with ~)",
)
def analyze_single(
    input_path: Path, output: Optional[Path], window_days: int, exclude_contacts: bool
):
    """Analyze a single WhatsApp group chat export."""
    logger.info(f"Analyzing single group: {input_path}")

    # Process the chat file
    df = chat_to_df(input_path)
    analysis = WhatsAppGroupAnalysis(df)

    # Get inactive users
    inactive_users = analysis.get_inactive_users(exclude_contacts=exclude_contacts)

    # Sort by total messages sent and then by joining date
    inactive_users = inactive_users.sort_values(
        by=["Total_Messages_Sent", "Joining_Date"], ascending=[True, True]
    )

    # Save or display results
    if output:
        inactive_users.to_csv(output, index=False)
        logger.info(f"Results saved to {output}")
    else:
        print("\nInactive Users:")
        print(inactive_users)


@cli.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
)
@click.option(
    "--output", "-o", type=click.Path(path_type=Path), help="Output file path"
)
@click.option(
    "--window-days", "-w", default=60, help="Window in days to consider for inactivity"
)
@click.option(
    "--exclude-contacts/--include-contacts",
    default=False,
    help="Exclude contacts (users with ~)",
)
def analyze_multiple(
    input_dir: Path, output: Optional[Path], window_days: int, exclude_contacts: bool
):
    """Analyze multiple WhatsApp group chat exports in a directory."""
    logger.info(f"Analyzing multiple groups in: {input_dir}")

    # Process all chat files
    chat_files = list(input_dir.glob("*.txt"))
    group_list = []
    for chat_file in chat_files:
        group_name = chat_file.stem
        chat_df = chat_to_df(chat_file, group_name=group_name)
        assert len(chat_df) > 0, f"Chat file {chat_file} is empty"
        group_list.append(chat_df)

    # Combine all groups
    combined_df = pd.concat(group_list, ignore_index=True)
    analysis = WhatsAppGroupAnalysis(combined_df)

    # Get inactive users
    inactive_users = analysis.get_inactive_users(exclude_contacts=exclude_contacts)

    # Sort by total messages sent and then by joining date
    inactive_users = inactive_users.sort_values(
        by=["Total_Messages_Sent", "Joining_Date"], ascending=[True, True]
    )

    # Save or display results
    if output:
        inactive_users.to_csv(output, index=False)
        logger.info(f"Results saved to {output}")
    else:
        print("\nInactive Users:")
        print(inactive_users)


@cli.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output", "-o", type=click.Path(path_type=Path), help="Output file path"
)
@click.option(
    "--window-days", "-w", default=60, help="Window in days to consider for inactivity"
)
@click.option(
    "--exclude-contacts/--include-contacts",
    default=False,
    help="Exclude contacts (users with ~)",
)
@click.option(
    "--decay-days", "-d", default=90, help="Number of days for score to decay to zero"
)
@click.option(
    "--reference-messages",
    "-r",
    default=5,
    help="Number of messages that would give a score of 1.0",
)
def score_inactive(
    input_path: Path,
    output: Optional[Path],
    window_days: int,
    exclude_contacts: bool,
    decay_days: int,
    reference_messages: int,
):
    """Analyze inactive users with an exponential decay activity score.

    This command helps identify formerly active members who might be worth re-activating
    by calculating an activity score based on their message history and recency.
    """
    logger.info(f"Scoring inactive users in: {input_path}")

    # Process the chat file
    df = chat_to_df(input_path)
    analysis = WhatsAppGroupAnalysis(df)

    # Get inactive users
    inactive_users = analysis.get_inactive_users(exclude_contacts=exclude_contacts)

    # Calculate activity scores
    scored_users = analysis.calculate_activity_score(
        inactive_users, decay_days=decay_days, reference_messages=reference_messages
    )

    # Save or display results
    if output:
        scored_users.to_csv(output, index=False)
        logger.info(f"Results saved to {output}")
    else:
        print("\nInactive Users with Activity Scores:")
        print(scored_users)


if __name__ == "__main__":
    cli()
