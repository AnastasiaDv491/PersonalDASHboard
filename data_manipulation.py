import numpy as np
import pandas as pd


def cleanDataforMap():
    df = pd.read_csv("data/sports_data.csv")

    def lat_lon(row):
        if row["Place"] == "Brussels":
            return [50.850346, 4.351721]
        if row["Place"] == "Zemst":
            return [50.984070, 4.464710]
        if row["Place"] == "Leuven":
            return [50.879845, 4.700518]
        if row["Place"] == "Moscow":
            return [55.755825, 37.617298]
        if row["Place"] == "Middelkerke":
            return [51.185139, 2.820850]
        if row["Place"] == "Mechelen":
            return [51.0281381, 4.4803453]
        if row["Place"] == "Wemmel":
            return [50.9092205, 4.3029931]
        if row["Place"] == "Vipiteno":
            return [46.8963235, 11.4319398]
        if row["Place"] == "Schmallenberg":
            return [51.1525937, 8.2836014]
        if row["Place"] == "Griante":
            return [45.995284, 9.235538]
        if row["Place"] == "Schaarbeek":
            return [50.8676041, 4.3737121]
        return "Unknown"

    df["Coord"] = df.apply(lat_lon, axis=1)
    coords = pd.DataFrame({"Count": df.groupby(["Place"]).size()}).reset_index()
    df2 = df[["Place", "Coord"]]
    df2 = df2[~df2.astype(str).duplicated()]
    df3 = pd.merge(coords, df2, on=["Place"])
    final_df = df3[df3["Coord"] != "Unknown"]

    return final_df
