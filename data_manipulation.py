import numpy as np
import pandas as pd
from pandas import TimedeltaIndex

df = pd.read_csv("data/sports_data.csv")

# Create dataframe for seasons


def cleanDataForSeason():
    df["Date"] = pd.to_datetime(df["Date"])

    def get_season(row):
        month = row["Date"].month
        if month in [12, 1, 2]:
            season = "Winter"
        elif month in [3, 4, 5]:
            season = "Spring"
        elif month in [6, 7, 8]:
            season = "Summer"
        elif month in [9, 10, 11]:
            season = "Autumn"

        return f"{season}"

    df["Season"] = df.apply(get_season, axis=1)
    return df


# Create dataframe for a map


def cleanDataforMap():
    def lat_lon(row):
        if row["Place"] == "Brussels":
            new_cols = pd.Series([[50.850346, 4.351721], "Belgium"])
        elif row["Place"] == "Zemst":
            new_cols = pd.Series([[50.984070, 4.464710], "Belgium"])
        elif row["Place"] == "Leuven":
            new_cols = pd.Series([[50.879845, 4.700518], "Belgium"])
        elif row["Place"] == "Moscow":
            new_cols = pd.Series([[55.755825, 37.617298], "Russia"])
        elif row["Place"] == "Middelkerke":
            new_cols = pd.Series([[51.185139, 2.820850], "Belgium"])
        elif row["Place"] == "Mechelen":
            new_cols = pd.Series([[51.0281381, 4.4803453], "Belgium"])
        elif row["Place"] == "Wemmel":
            new_cols = pd.Series([[50.9092205, 4.3029931], "Belgium"])
        elif row["Place"] == "Vipiteno":
            new_cols = pd.Series([[46.8963235, 11.4319398], "Italy"])
        elif row["Place"] == "Schmallenberg":
            new_cols = pd.Series([[51.1525937, 8.2836014], "Germany"])
        elif row["Place"] == "Griante":
            new_cols = pd.Series([[45.995284, 9.235538], "Italy"])
        elif row["Place"] == "Schaarbeek":
            new_cols = pd.Series([[50.8676041, 4.3737121], "Belgium"])
        else:
            new_cols = pd.Series(["Unknown", "Unknown"])
        return new_cols

    df[["Coord", "Country"]] = df.apply(lat_lon, axis=1)
    coords = pd.DataFrame({"Count": df.groupby(["Place"]).size()}).reset_index()
    df2 = df[["Place", "Coord", "Country"]]
    df2 = df2[~df2.astype(str).duplicated()]
    df3 = pd.merge(coords, df2, on=["Place"])
    final_df = df3[df3["Coord"] != "Unknown"]
    return final_df


# Quick Facts data


def getTrainingStats():
    df_quick_stats = df
    df_quick_stats["Avg HR"] = pd.to_numeric(df["Avg HR"].replace("--", "0"))
    calories = df["Calories"].str.replace("--", "0")
    df_quick_stats["Calories"] = pd.to_numeric(calories.str.replace(",", "."))

    # Running stats
    df_running = df_quick_stats[df_quick_stats["Activity Type"].isin(["Running"])]
    time = TimedeltaIndex(pd.to_datetime(df_running["Time"]).dt.strftime("%H:%M:%S"))

    running_time_total = round(time.sum() / np.timedelta64(1, "h"))  # total hours
    running_avg_hr = round(df_running.loc[:, "Avg HR"].mean())  # avg heart rate
    running_avg_calories = round(df_running.loc[:, "Calories"].mean())  # avg calories

    speed = df_running["Avg Speed"].str.strip("'")  # avg speed
    speed = pd.to_timedelta("00:" + speed)
    totsec = speed.mean().total_seconds()
    m = round((totsec % 3600) // 60)
    sec = round((totsec % 3600) % 60)
    running_avg_speed = f"{m}:{sec}"

    # Strength training stats
    df_strength = df_quick_stats[
        df_quick_stats["Activity Type"].isin(["Strength Training"])
    ]
    time2 = TimedeltaIndex(pd.to_datetime(df_strength["Time"]).dt.strftime("%H:%M:%S"))

    strength_total = round(time2.sum() / np.timedelta64(1, "h"))  # total hours
    strength_avg_hr = round(df_strength.loc[:, "Avg HR"].mean())  # avg heart rate
    strength_avg_calories = round(df_strength.loc[:, "Calories"].mean())  # avg calories

    totsec = time2.mean().total_seconds()  # avg time training
    m = round((totsec % 3600) // 60)
    sec = round((totsec % 3600) % 60)
    strength_avg_time = f"{m}:{sec}"

    # create dict
    running_dict = dict()
    running_dict["Total Hours Running"] = running_time_total
    running_dict["Avg. Heart Rate"] = running_avg_hr
    running_dict["Avg. Calories Burnt"] = running_avg_calories
    running_dict["Avg. Speed"] = running_avg_speed

    strength_dict = dict()
    strength_dict["Total Hours Trained"] = strength_total
    strength_dict["Avg. Heart Rate"] = strength_avg_hr
    strength_dict["Avg. Calories"] = strength_avg_calories
    strength_dict["Avg. Time Trained"] = strength_avg_time

    return running_dict, strength_dict
