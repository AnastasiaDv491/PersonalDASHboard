# Data: fakbars, events, mic_locations
import pandas as pd
import plotly.graph_objects as go
from io import StringIO
import dash
from dash import Input, Output, dcc, html, Dash
import numpy as np
from data_manipulation import cleanDataforMap

df = pd.read_csv("data/sports_data.csv")

# First graph


# Create filters
def buildYearFilter():
    filters = html.Div(
        [
            dcc.Dropdown(
                options=pd.to_datetime(df["Date"]).dt.year.unique(),
                value=2023,
                className="page2-dropdown",
                id="dropdownYear",
            ),
        ],
        className="filters_parent",
    )
    return filters


def buildYearGraph():
    div = html.Div(
        className="graph_div",
        children=[
            dcc.Store(id="memory-output1"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id="graph-id1",
            ),
        ],
    )
    return div


@dash.callback(
    Output("memory-output1", "data"),
    Input("dropdownYear", "value"),
)
def data(value):
    df = pd.read_csv("data/sports_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    df["Year"] = df["Date"].dt.year

    filter_df = df[df["Year"] == value]
    rslt_df = pd.DataFrame(
        {"Count": filter_df.groupby(["Activity Type"]).size()}
    ).reset_index()

    return rslt_df.to_dict("records")


@dash.callback(Output("graph-id1", "figure"), Input("memory-output1", "data"))
def create_pie_chart(rslt_df):
    rslt_df = pd.DataFrame(rslt_df)
    fig = go.Figure(
        data=[go.Pie(labels=rslt_df["Activity Type"], values=rslt_df["Count"])]
    )
    return fig


# Second Graph
df = pd.read_csv("data/sports_data.csv")

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


# Creating filters
def buildSeasonFilter():
    filters = html.Div(
        [
            dcc.Dropdown(
                options=df["Season"].unique(),
                value="Summer",
                className="page2-dropdown",
                id="dropdownSeason",
            ),
        ],
        className="filters_parent",
    )
    return filters


def buildSeasonGraph():
    div = html.Div(
        className="graph_div",
        children=[
            dcc.Store(id="memory-output2"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id="graph-id2",
            ),
        ],
    )
    return div


@dash.callback(
    Output("memory-output2", "data"),
    Input("dropdownSeason", "value"),
)
def data(value):
    df = pd.read_csv("data/sports_data.csv")
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

    filter_df = df[df["Season"] == value]
    rslt_df = pd.DataFrame(
        {"Count": filter_df.groupby(["Activity Type"]).size()}
    ).reset_index()

    return rslt_df.to_dict("records")


@dash.callback(Output("graph-id2", "figure"), Input("memory-output2", "data"))
def create_pie_chart(rslt_df):
    rslt_df = pd.DataFrame(rslt_df)
    fig = go.Figure(
        data=[go.Pie(labels=rslt_df["Activity Type"], values=rslt_df["Count"])]
    )
    return fig


# Third Graph

# Create filters

map_df = cleanDataforMap()


def buildMap():
    div = html.Div(
        className="graph_div",
        children=[
            dcc.Store(id="memory-output3"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id="line-fig",
                figure=go.Figure().add_trace(
                    go.Scattergeo(
                        lon=map_df["Coord"].str[1],
                        lat=map_df["Coord"].str[0],
                        marker=dict(
                            size=map_df["Count"] * 4,
                            line_color="rgb(40,40,40)",
                            line_width=0.5,
                            sizemode="area",
                        ),
                    )
                ),
            ),
        ],
    )
    return div
