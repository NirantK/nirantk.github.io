import re
from datetime import datetime, timedelta
from typing import List, Tuple
from pathlib import Path
import pandas as pd


class MessageExtractor:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def extract_messages(self) -> List[Tuple[str, str, str]]:
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


class TopSenders:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def top_k_senders(self, freq: str, k: int = 5) -> pd.DataFrame:
        resampled = self.df.groupby("Sender").resample(freq).count()
        sorted_grouped = (
            resampled["Message"]
            .reset_index()
            .sort_values(["Datetime", "Message"], ascending=[True, False])
            .groupby("Datetime")
        )
        top_senders = sorted_grouped.head(k)
        return top_senders


class WeeklySenders:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def compute_weekly_sender_stats(self) -> None:
        # Assuming 'df' is the DataFrame with the columns 'Sender', 'Datetime', and 'Message'
        # Make sure the 'Datetime' column is set as the index
        self.df.set_index("Datetime", inplace=True)
        self.df.sort_index(inplace=True)

        # Resample DataFrame to a weekly frequency
        weekly_data = self.df.resample("W").count()

        # Initialize lists to store the counts
        new_senders, active_senders, churned_senders = [], [], []

        # Initialize sets for active and churned senders
        current_senders, previous_senders, churned = set(), set(), set()

        # Time window to consider a sender as churned (21 days)
        churn_window = timedelta(days=21)

        # Iterate through each week
        for week in weekly_data.index:
            # Get the data for the current week
            current_week_data = self.df.truncate(
                before=week - timedelta(weeks=1) + timedelta(seconds=1), after=week
            )

            # Calculate new, active, and churned senders for the current week
            new_senders_count, active_senders_count, churned_senders_count = 0, 0, 0

            for sender in current_week_data["Sender"].unique():
                # Check if the sender is new
                if sender not in current_senders and sender not in previous_senders:
                    new_senders_count += 1
                    current_senders.add(sender)

                # Check if the sender is active
                if sender in current_senders or sender in previous_senders:
                    active_senders_count += 1
                    current_senders.add(sender)

            # Update churned senders
            for sender in previous_senders:
                if (
                    sender not in current_senders
                    and (week - df[df["Sender"] == sender].index[-1]) > churn_window
                ):
                    churned_senders_count += 1
                    churned.add(sender)

            # Store the results in the lists
            new_senders.append(new_senders_count)
            active_senders.append(active_senders_count)
            churned_senders.append(churned_senders_count)

            # Update previous_senders for the next iteration
            previous_senders.update(current_senders)
            current_senders.clear()

            result_df = pd.DataFrame(
                {
                    "Date": weekly_data.index,
                    "New Senders": new_senders,
                    "Active Senders": active_senders,
                    "Churned Senders": churned_senders,
                }
            )
        result_df.set_index("Date", inplace=True)


if __name__ == "__main__":
    readpath = Path("_chat.txt")
    msg_extractor = MessageExtractor(readpath)
    messages = msg_extractor.extract_messages()
    df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])
    top_senders = TopSenders(df)
    weekly_senders = WeeklySenders(df)

    # Top K senders per week
    k = 6
    top_senders_weekly = top_senders.top_k_senders("W", k)
    print(f"Top {k} senders per week:")

    # Top K senders per month
    top_senders_monthly = top_senders.top_k_senders("M", k)
    print(f"\nTop {k} senders per month:")
    display(top_senders_monthly.style.hide_index())

    # Weekly stats for new, active and churned senders.
    weekly_sender_stats = weekly_senders.compute_weekly_sender_stats()
    display(weekly_sender_stats)
