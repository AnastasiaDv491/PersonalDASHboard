import numpy as np
import pandas as pd

df = pd.read_csv("data/sports_data.csv")
df_running = df[df["Activity Type"].isin(["Running", "Treadmill Running"])]

# Average Heart Rate calculation


def avg_hr_graph():
    df2 = df_running
    df2["Avg HR"] = pd.to_numeric(df["Avg HR"].replace("--", "0"))
    df2["Date"] = pd.to_datetime(df2["Date"])
    df2["MonthYear"] = df2["Date"].dt.to_period("M")

    grouped = df2.groupby(["MonthYear"])["Avg HR"].mean()
    df_new = grouped.reset_index()

    df_new["MonthYear"] = df_new["MonthYear"].astype(str)
    df_new["MonthYear"] = pd.to_datetime(df_new["MonthYear"])

    return df_new


# Running Distance


def running_distance():
    df2 = df_running
    df2["Distance"] = df2["Distance"].astype(str)
    df2 = df2[df2["Distance"].str.contains(r"(\d*)\.(\d*)")]

    df2["Distance"] = pd.to_numeric(df["Distance"].replace("--", "0"))
    df2 = df2[df2.Distance != 0]
    df2["Date"] = pd.to_datetime(df2["Date"])
    df2["MonthYear"] = df2["Date"].dt.to_period("M")
    return df2


# Running Aerpbic TE


def running_aerobic_te():
    df2 = df_running
    df2["Aerobic TE"] = pd.to_numeric(df["Aerobic TE"].replace("--", "0"))
    df2["Date"] = pd.to_datetime(df2["Date"])
    df2["MonthYear"] = df2["Date"].dt.to_period("M")
    df2 = df2[df2["Aerobic TE"] != 0]

    grouped = df2.groupby(["MonthYear"])["Aerobic TE"].mean()  # don't reset the index!
    df_new = grouped.reset_index()

    df_new["MonthYear"] = df_new["MonthYear"].astype(str)
    df_new["MonthYear"] = pd.to_datetime(df_new["MonthYear"])

    return df_new
