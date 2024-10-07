import pandas as pd
import plotly.graph_objects as go
from io import StringIO
import dash
from dash import Input, Output, dcc, html, Dash
import numpy as np
import dash_bootstrap_components as dbc
import plotly.express as px
from data_processing.data_manipulation_running import (
    avg_hr_graph,
    running_distance,
    running_aerobic_te,
)


# Line graph for Avg HR
avg_hr_df = avg_hr_graph()
distance_df = running_distance()
aer_te_df = running_aerobic_te()


def buildAvgHRGraph():
    div = html.Div(
        className="graph_div graph_div_line_avghr",
        children=[
            html.Br(),
            dcc.Graph(
                id="line-fig",
                figure=px.line(
                    avg_hr_df,
                    x="MonthYear",
                    y="Avg HR",
                    title="Эволюция Cреднего Cердечного Pитма.",
                    labels={
                        "MonthYear": "Дата (Месяц-Год)",
                        "Avg HR": "Средний Сердечный Ритм",
                    },
                    height=500,
                    width=1000,
                ),
            ),
        ],
    )
    return div


def buildDistanceGraph():
    div = html.Div(
        className="graph_div graph_div_line_dist",
        children=[
            dcc.Graph(
                id="line-fig",
                figure=px.line(
                    distance_df,
                    x="Date",
                    y="Distance",
                    title="Эволюция Беговой Дистанции.",
                    labels={
                        "Date": "Дата (Месяц-Год)",
                        "Distance": "Дистанция",
                    },
                    height=500,
                    width=1000,
                ),
            ),
        ],
    )
    return div


def buildAerGraph():
    div = html.Div(
        className="graph_div graph_div_line_aer",
        children=[
            dcc.Graph(
                id="line-fig",
                figure=px.line(
                    aer_te_df,
                    x="MonthYear",
                    y="Aerobic TE",
                    title="Эволюция Среднего Аэробного Обмена.",
                    labels={
                        "MonthYear": "Дата (Месяц-Год)",
                        "Aerobic TE": "Средний Аэробный Обмен",
                    },
                    height=500,
                    width=1000,
                )
                .add_hrect(
                    y0=0.0,
                    y1=1.0,
                    line_width=0,
                    fillcolor="#dcf6bd",
                    opacity=0.2,
                    annotation_text="нет эффекта",
                )
                .add_hrect(
                    y0=1.0,
                    y1=2.0,
                    line_width=0,
                    fillcolor="#a0f950",
                    opacity=0.2,
                    annotation_text="маленький эффект",
                )
                .add_hrect(
                    y0=2.0,
                    y1=3.0,
                    line_width=0,
                    fillcolor="#f9db50",
                    opacity=0.2,
                    annotation_text="поддерживающий эффект",
                )
                .add_hrect(
                    y0=3.0,
                    y1=4.0,
                    line_width=0,
                    fillcolor="#f64624",
                    opacity=0.2,
                    annotation_text="развивающий эффект",
                )
                .add_hrect(
                    y0=4.0,
                    y1=4.9,
                    line_width=0,
                    fillcolor="#f71c0c",
                    opacity=0.4,
                    annotation_text="высокий развивающий эффект",
                ),
            ),
        ],
    )
    return div
