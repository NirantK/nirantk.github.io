import pandas as pd

from formatting_functions import human_date


def generate_daily_df(readpath: str, return_df: bool = False) -> None:
    df = pd.read_csv(readpath)
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df["Date"] = df["Datetime"].dt.date
    daily_df = df.groupby("Date").agg({"Message": " \n ".join}).reset_index()
    daily_df["wc"] = daily_df["Message"].apply(lambda x: len(x.split()))
    d = daily_df["Date"][42]
    print(human_date(d))
    print(daily_df["wc"].describe())
    if return_df:
        return daily_df


if __name__ == "__main__":
    readpath = "20230507_Messages.csv"
    generate_daily_df(readpath)
