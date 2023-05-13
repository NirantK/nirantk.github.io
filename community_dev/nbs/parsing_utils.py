import datetime
import re
from pathlib import Path

from pydantic import BaseModel


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
                    dt = datetime.strptime(datetime_str, "%m/%d/%y %H:%M:%S")
                    messages.append((sender, dt, message))
        return messages


class PIIRemover:
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


class DataFrameCleaner:
    def __init__(self, df):
        self.df = df

    def cleanup(self):
        # Drop the Sender column
        if "Sender" in self.df.columns:
            self.df = self.df.drop(columns=["Sender"])
        # Drop the rows with no message
        self.df = self.df.dropna()

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

        for s in to_remove:
            self.df = self.df[~self.df["Message"].str.contains(s)]

        pii_remover = PIIRemover()
        self.df["Message"] = self.df["Message"].apply(pii_remover.remove_pii)

        return self.df
