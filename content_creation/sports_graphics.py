import pandas as pd
import plotly.graph_objects as go
from io import StringIO
import dash
from dash import Input, Output, dcc, html, Dash
import numpy as np
from data_processing.data_manipulation import (
    cleanDataForSeason,
    cleanDataforMap,
    getTrainingStats,
)
import dash_bootstrap_components as dbc

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


df_season = cleanDataForSeason()


# Creating filters
def buildSeasonFilter():
    filters = html.Div(
        [
            dcc.Dropdown(
                options=df_season["Season"].unique(),
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
    df = cleanDataForSeason()

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
        className="graph_div graph_div_map",
        children=[
            dcc.Store(id="memory-output3"),
            html.Br(),
            html.H4("Топ-3 мест Бега: "),
            html.Ul(
                id="map_list",
                children=[
                    html.Li(i)
                    for i in map_df.sort_values(by=["Count"], ascending=False)["Place"][
                        0:3
                    ]
                ],
            ),
            dcc.Graph(
                id="line-fig",
                figure=go.Figure()
                .add_trace(
                    go.Scattergeo(
                        locationmode="country names",
                        locations=map_df["Country"],
                        lon=map_df["Coord"].str[1],
                        lat=map_df["Coord"].str[0],
                        text=map_df["Count"],
                        marker=dict(
                            size=map_df["Count"] * 10,
                            line_color="rgb(40,40,40)",
                            line_width=0.5,
                            sizemode="area",
                        ),
                    )
                )
                .update_geos(scope="europe"),
            ),
        ],
    )
    return div


# Fourth Graph ( Quick Stats)

running_dict, strength_dict = getTrainingStats()


def buildQuickFacts():
    div = html.Div(
        className="graph_div",
        children=[
            # dcc.Store(id="memory-output4"),
            html.Br(),
            html.Div(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H1(f"{next(iter(running_dict.values()))}"),
                                        html.P(f"{next(iter(running_dict))}"),
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.Ul(
                                            id="map_list",
                                            children=[
                                                html.Li(f"{k}: {v}")
                                                for k, v in running_dict.items()
                                                if k != "Кол.во Часов Бега"
                                            ],
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H1(
                                            f"{next(iter(strength_dict.values()))}"
                                        ),
                                        html.P(f"{next(iter(strength_dict))}"),
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.Ul(
                                            id="map_list",
                                            children=[
                                                html.Li(f"{k}: {v}")
                                                for k, v in strength_dict.items()
                                                if k
                                                != "Кол.во Часов Силовых тренировок"
                                            ],
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                ]
            ),
        ],
    )
    return div
