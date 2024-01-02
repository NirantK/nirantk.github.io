import re
from datetime import datetime
from pathlib import Path
from typing import Tuple

import pandas as pd


def extract_messages(file_path: Path) -> pd.DataFrame:
    """
    Extract messages from a WhatsApp chat file.

    :param file_path: Path to the WhatsApp chat file.
    :return: DataFrame containing Sender, Datetime, and Message columns.
    """
    # Pattern to match the WhatsApp messages
    pattern = re.compile(
        r"\[(?P<date>\d{1,2}\/\d{1,2}\/\d{2,4}), (?P<time>\d{1,2}:\d{2}:\d{2})\] (?P<sender>[^:]+): (?P<message>.+)"
    )

    # Lists to hold the extracted data with consideration for multi-line messages
    dates = []
    times = []
    senders = []
    messages = []

    # Variables to hold the current message details
    current_date = current_time = current_sender = current_message = None

    # Reading the file and extracting the messages, considering multi-line messages
    with open(file_path, "r") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                if current_message is not None:
                    dates.append(current_date)
                    times.append(current_time)
                    senders.append(current_sender)
                    messages.append(current_message)
                current_date = match.group("date")
                current_time = match.group("time")
                current_sender = match.group("sender")
                current_message = match.group("message")
            else:
                if current_message is not None:
                    current_message += " " + line.strip()

    # Adding the last message if there is one
    if current_message is not None:
        dates.append(current_date)
        times.append(current_time)
        senders.append(current_sender)
        messages.append(current_message)

    # Combining the date and time into a single datetime column
    datetimes = [
        datetime.strptime(f"{date} {time}", "%m/%d/%y %H:%M:%S")
        for date, time in zip(dates, times)
    ]

    # Creating a DataFrame with multi-line messages
    chat_df = pd.DataFrame(
        {"Sender": senders, "Datetime": datetimes, "Message": messages}
    )

    return chat_df


def cleanup(df):
    # Drop the rows with no message
    # df = df.dropna()
    df = df.drop_duplicates(subset=["Datetime", "Sender", "Message"])
    df = df.sort_values(by="Datetime")
    df = df[~df["Message"].str.contains("deleted this message")]
    df = df[~df["Message"].str.contains("message was deleted")]
    df = df[~df["Message"].str.contains("changed the subject to")]
    # df = df[~df["Message"].str.contains("You added")]
    df = df[~df["Message"].str.contains("changed the group description")]
    df = df[~df["Message"].str.contains("reset this group's invite link")]
    df = df[~df["Message"].str.contains("changed this group's icon")]
    df = df[~df["Message"].str.contains("changed the subject from")]
    df = df[~df["Message"].str.contains("changed this group's settings")]
    df["Message"] = df["Message"].apply(remove_pii)
    return df


def remove_pii(text):
    # Remove phone numbers
    phone_pattern = re.compile(r"@\+?(\d[\d-]{7,}\d)")
    no_phones = phone_pattern.sub("[PHONE]", text)

    # Remove email addresses
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    no_emails = email_pattern.sub("[EMAIL]", no_phones)

    return no_emails


class WhatsAppGroupAnalysis:
    def __init__(self, df: pd.DataFrame):
        # Read the CSV file
        self.df = df
        # Convert the 'Datetime' column to a datetime object
        self.df["Datetime"] = pd.to_datetime(self.df["Datetime"])


# Redefining the entire class with all methods and their full implementations


class WhatsAppGroupAnalysis:
    def __init__(self, df):
        self.df = df
        # Convert the 'Datetime' column to a datetime object
        self.df["Datetime"] = pd.to_datetime(self.df["Datetime"])

    def get_current_users(self) -> Tuple[pd.DataFrame, int]:
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
        return current_users_df, current_users_count

    def get_message_count_in_window(self, window_days: int = 60) -> pd.DataFrame:
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
        return message_count_in_window

    def get_users_with_zero_messages(self) -> pd.DataFrame:
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
        return users_with_zero_messages

    def get_users_with_joining_date(self) -> pd.DataFrame:
        # Identifying pattern for joining or being added
        joining_pattern = self.df["Message"].str.contains(
            "joined using this group|added", case=False, na=False
        )
        # Extracting joining dates and users
        joining_dates_df = self.df[joining_pattern][["Sender", "Datetime"]].copy()
        joining_dates_df.columns = ["User", "Joining_Date"]
        # Keep the earliest joining date for each user
        users_with_joining_date = joining_dates_df.groupby("User").min().reset_index()
        return users_with_joining_date

    def get_inactive_users(self, exclude_contacts: bool = False) -> pd.DataFrame:
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
        return filtered_inactive_users_with_recent_message
