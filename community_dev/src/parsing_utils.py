import datetime
import re
from pathlib import Path
from typing import List, Tuple, Union

import pandas as pd
from loguru import logger
from pydantic import BaseModel


class WhatsAppMessageExtractor(BaseModel):
    """
    Extracts messages from a WhatsApp chat export file
    into a list of tuples: (sender, datetime, message)
    """

    file_path: Path

    def extract_messages(self) -> List[Tuple[str, datetime.datetime, str]]:
        """
        Extracts messages from a WhatsApp chat export file
        into a list of tuples: (sender, datetime, message)
        
        Returns:
            List of tuples containing (sender, datetime, message)
        """
        pattern = re.compile(
            r"\[(?P<date>\d{1,2}\/\d{1,2}\/\d{2,4}), (?P<time>\d{1,2}:\d{2}:\d{2})\] (?P<sender>[^:]+): (?P<message>.+)"
        )
        join_pattern = re.compile(r"joined using this group\'s invite link")
        messages = []
        
        logger.info(f"Extracting messages from {self.file_path}")
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.match(line)
                if match and not join_pattern.search(line):
                    date, time, sender, message = match.groups()
                    datetime_str = f"{date} {time}"
                    dt = datetime.datetime.strptime(datetime_str, "%m/%d/%y %H:%M:%S")
                    messages.append((sender, dt, message))
        
        logger.info(f"Extracted {len(messages)} messages")
        df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])
        messages = self.remove_actions(df)
        return messages

    def remove_pii(self, text: str) -> str:
        """
        Remove personally identifiable information from text.
        
        Args:
            text: Text to remove PII from
            
        Returns:
            Text with PII removed
        """
        # Remove phone numbers
        phone_pattern = re.compile(r"@\+?(\d[\d-]{7,}\d)")
        no_phones = phone_pattern.sub("[PHONE REMOVED]", text)

        # Remove email addresses
        email_pattern = re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        )
        no_emails = email_pattern.sub("[EMAIL REMOVED]", no_phones)

        return no_emails

    def remove_actions(self, df: pd.DataFrame, remove_sender: bool = False) -> List[Tuple[str, datetime.datetime, str]]:
        """
        Remove system actions and clean up the DataFrame.
        
        Args:
            df: DataFrame containing message data
            remove_sender: Whether to remove the Sender column, defaults to False
            
        Returns:
            List of tuples containing (sender, datetime, message)
        """
        # Drop the Sender column
        logger.info(f"Dataframe columns: {df.columns}")
        if "Sender" in df.columns and remove_sender:
            df = df.drop(columns=["Sender"])
        # Drop the rows with no message
        df.dropna(inplace=True)
        logger.info(f"Number of messages before removing actions: {len(df)}")

        to_remove = [
            "deleted this message",
            "message was deleted",
            "‎‪",  # Not sure about this, notebooks rendered them properly, so does VSCode
            "changed the subject to",
            "‎",  # Not sure about this, notebooks rendered them properly, so does VSCode
            "You added",
            "changed the group description",
            "POLL:",
            "reset this group's invite link",
            "changed this group's icon",
            "changed the subject from",
            "changed this group's settings",
        ]

        for stop_phrase in to_remove:
            df = df[~df["Message"].str.contains(stop_phrase)]
            
        logger.info(f"Number of messages after removing actions: {len(df)}")
        
        # Convert DataFrame back to list of tuples
        return list(df.itertuples(index=False, name=None))
