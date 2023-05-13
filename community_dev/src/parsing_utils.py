import datetime
import re
from pathlib import Path

import loguru
import pandas as pd
from pydantic import BaseModel

logger = loguru.logger


class WhatsAppMessageExtractor(BaseModel):
    """
    Extracts messages from a WhatsApp chat export file
    into a list of tuples: (sender, datetime, message)
    """

    file_path: Path

    def extract_messages(self) -> list[tuple[str, str, str]]:
        """
        Extracts messages from a WhatsApp chat export file
        into a list of tuples: (sender, datetime, message)
        """
        pattern = re.compile(
            r"\[(?P<date>\d{1,2}\/\d{1,2}\/\d{2,4}), (?P<time>\d{1,2}:\d{2}:\d{2})\] (?P<sender>[^:]+): (?P<message>.+)"
        )
        join_pattern = re.compile(r"joined using this group\'s invite link")
        messages = []
        with open(self.file_path, "r") as f:
            for line in f:
                match = pattern.match(line)
                if match and not join_pattern.search(line):
                    date, time, sender, message = match.groups()
                    datetime_str = f"{date} {time}"
                    dt = datetime.datetime.strptime(datetime_str, "%m/%d/%y %H:%M:%S")
                    messages.append((sender, dt, message))
        df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])
        messages = self.remove_actions(df)
        return messages

    def remove_pii(self, text):
        # Remove phone numbers
        phone_pattern = re.compile(r"@\+?(\d[\d-]{7,}\d)")
        no_phones = phone_pattern.sub("[PHONE REMOVED]", text)

        # Remove email addresses
        email_pattern = re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        )
        no_emails = email_pattern.sub("[EMAIL REMOVED]", no_phones)

        return no_emails

    def remove_actions(self, df, remove_sender=False) -> None:
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
