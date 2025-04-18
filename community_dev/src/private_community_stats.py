from datetime import timedelta
from pathlib import Path
from typing import List, Tuple, Union

import fire
import pandas as pd
from loguru import logger
from rich import print
from tqdm import tqdm

from parsing_utils import WhatsAppMessageExtractor


def get_top_senders(df: pd.DataFrame, freq: str, k: int = 5) -> pd.DataFrame:
    """Get the top K senders per week or month.

    Args:
        df: DataFrame containing message data with 'Sender' and 'Datetime' columns
        freq: Frequency for resampling, either 'W' (week) or 'M' (month)
        k: Number of top senders to return, defaults to 5

    Returns:
        DataFrame containing the top k senders for each time period

    Raises:
        ValueError: If freq is not 'W' or 'M'
    """
    if freq not in ["W", "M"]:
        raise ValueError("freq must be 'W' or 'M'")
    
    # If 'Datetime' is not the index, set it as the index
    logger.info(f"Index name: {df.index.name}, type: {type(df.index)}")
    if df.index.name != "Datetime":
        df["Datetime"] = pd.to_datetime(df["Datetime"])
        df.set_index("Datetime", inplace=True)  # Set 'Datetime' as index
        df.sort_index(inplace=True)  # Sort the DataFrame based on the index
        logger.info(f"Index name: {df.index.name}, type: {type(df.index)}")
    
    resampled = df.groupby("Sender").resample(freq).count()
    resampled.reset_index("Datetime", inplace=True)  # Reset only the 'Datetime' index
    sorted_grouped = (
        resampled["Message"]
        .reset_index()
        .sort_values(["Datetime", "Message"], ascending=[True, False])
        .groupby("Datetime")
    )
    top_senders = sorted_grouped.head(k)
    return top_senders


class ActivityStats:
    """Class for computing activity statistics from message data."""

    def __init__(self, df: pd.DataFrame) -> None:
        """Initialize with a DataFrame containing message data.

        Args:
            df: DataFrame with 'Datetime' and 'Sender' columns
        """
        self.df = df
        if self.df.index.name != "Datetime":
            self.df.set_index("Datetime", inplace=True)
            self.df.sort_index(inplace=True)

    def compute_sender_stats(self) -> pd.DataFrame:
        """Compute statistics about sender activity over time.

        Returns:
            DataFrame with weekly counts of new, active, and churned senders
        """
        # Resample DataFrame to a weekly frequency
        weekly_data = self.df.resample("W").count()

        # Initialize lists to store the counts
        new_senders: List[int] = []
        active_senders: List[int] = []
        churned_senders: List[int] = []

        # Initialize sets for active and churned senders
        current_senders: set = set()
        previous_senders: set = set()
        churned: set = set()

        # Time window to consider a sender as churned (21 days)
        churn_window = timedelta(days=21)

        # Iterate through each week
        for week in tqdm(weekly_data.index, desc="Computing sender stats"):
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
                    and (week - self.df[self.df["Sender"] == sender].index[-1])
                    > churn_window
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
        return result_df


def compute(readpath: Union[str, Path], k: int = 5) -> None:
    """Compute community statistics from WhatsApp chat data.

    Args:
        readpath: Path to the WhatsApp chat file
        k: Number of top senders to consider, defaults to 5
    """
    readpath = Path(readpath)
    assert readpath.exists(), f"File not found: {readpath}"
    
    logger.info(f"Processing WhatsApp chat file: {readpath}")
    msg_extractor = WhatsAppMessageExtractor(file_path=readpath)
    messages = msg_extractor.extract_messages()
    df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])

    # Top K senders per week
    logger.info("Computing weekly top senders")
    weekly_top_senders = get_top_senders(df, freq="W", k=k)
    print(f"Top {k} senders per week:\n{weekly_top_senders}")

    # Top K senders per month
    logger.info("Computing monthly top senders")
    monthly_top_senders = get_top_senders(df, freq="M", k=k)
    print(f"Top {k} senders per month:\n{monthly_top_senders}")

    # Compute sender statistics
    logger.info("Computing sender statistics")
    weekly_senders = ActivityStats(df)
    stats_df = weekly_senders.compute_sender_stats()
    print("Weekly sender stats:")
    print(stats_df)


if __name__ == "__main__":
    fire.Fire(compute)
