import re
from pathlib import Path

import pandas as pd

from private_community_stats import MessageExtractor


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


if __name__ == "__main__":
    readpath = Path("_chat.txt")

    # Today's date
    todays_date = df["Datetime"].max().date().strftime("%Y%m%d")
    print(f"Today's date is {todays_date}")

    savepath = f"../{todays_date}_Messages.csv"

    msg_extractor = MessageExtractor(readpath)
    messages = msg_extractor.extract_messages()
    df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])
    print(f"Before cleanup: {len(df)}")
    df_cleaner = DataFrameCleaner(df)
    df = df_cleaner.cleanup()
    print(f"After cleanup: {len(df)}")

    df.to_csv(savepath, index=False)
