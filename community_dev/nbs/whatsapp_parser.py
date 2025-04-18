import re
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Union

import pandas as pd
from loguru import logger
from tqdm import tqdm


def extract_dataframe(file_path: Union[str, Path]) -> pd.DataFrame:
    """Extract message data from a WhatsApp chat export file.
    
    Args:
        file_path: Path to the WhatsApp chat export file
        
    Returns:
        DataFrame containing message data with columns: Datetime, Sender, Message
    """
    datetimes, senders, messages = [], [], []
    
    message_patterns = [
        r'\[(\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2})\]([^:]+): (.+)',
        r'(\d{2}/\d{2}/\d{2},\s+\d{1,2}:\d{2}\s+[ap]m)([^:]+): (.+)?',
    ]
    system_pattern = r'\[(\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2})\] (.+)'
    
    def parse_datetime(date_str: str) -> datetime:
        """Parse a datetime string into a datetime object.
        
        Args:
            date_str: String containing date and time
            
        Returns:
            Datetime object
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d, %H:%M:%S')
        except ValueError:
            return datetime.strptime(date_str, '%d/%m/%y, %I:%M %p')
    
    file_path = Path(file_path)
    logger.info(f"Extracting data from {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in tqdm(file, desc="Processing lines"):
            line = line.strip()
            
            for pattern in message_patterns:
                match = re.match(pattern, line)
                if match:
                    date_str, sender, message = match.groups()
                    date_time = parse_datetime(date_str)
                    break
            else:
                system_match = re.match(system_pattern, line)
                if system_match:
                    date_str, message = system_match.groups()
                    date_time = parse_datetime(date_str)
                    sender = 'System or Continuation'
                continue
            
            datetimes.append(date_time)
            senders.append(sender)
            messages.append(message)

    logger.info(f"Extracted {len(datetimes)} messages")
    return pd.DataFrame({
        "Datetime": datetimes,
        "Sender": senders,
        "Message": messages,
    })
    
def cleanup(df: pd.DataFrame) -> pd.DataFrame:
    """Clean up the DataFrame by removing system messages and duplicates.
    
    Args:
        df: DataFrame containing message data
        
    Returns:
        Cleaned DataFrame
    """
    # Drop the rows with no message
    # df = df.dropna()
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
    
    # Remove PII
    df["Message"] = df["Message"].apply(remove_pii)
    
    logger.info(f"Cleaned DataFrame has {len(df)} messages")
    return df


def remove_pii(text: str) -> str:
    """Remove personally identifiable information from text.
    
    Args:
        text: Text to remove PII from
        
    Returns:
        Text with PII removed
    """
    # Remove phone numbers
    phone_pattern = re.compile(r"@\+?(\d[\d-]{7,}\d)")
    no_phones = phone_pattern.sub("[PHONE]", text)

    # Remove email addresses
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    no_emails = email_pattern.sub("[EMAIL]", no_phones)

    return no_emails


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
        logger.info(f"Message counts calculated for {len(message_count_in_window)} users in {window_days} day window")
        return message_count_in_window

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
        logger.info(f"Found {len(filtered_inactive_users_with_recent_message)} inactive users")
        return filtered_inactive_users_with_recent_message
