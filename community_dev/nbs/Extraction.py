import re
from pathlib import Path

import pandas as pd

from parsing_utils import MessageExtractor, DataFrameCleaner


if __name__ == "__main__":
    readpath = Path("_chat.txt")

    # Today's date
    latest_date = df["Datetime"].max().date().strftime("%Y%m%d")
    print(f"Today's date is {latest_date}")

    savepath = f"../{latest_date}_Messages.csv"

    msg_extractor = MessageExtractor(readpath)
    messages = msg_extractor.extract_messages()
    df = pd.DataFrame(messages, columns=["Sender", "Datetime", "Message"])
    print(f"Before cleanup: {len(df)}")
    df_cleaner = DataFrameCleaner(df)
    df = df_cleaner.cleanup()
    print(f"After cleanup: {len(df)}")

    df.to_csv(savepath, index=False)
