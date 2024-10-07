from dash import (
    html,
    register_page,
)  # , callback # If you need callbacks, import it here.

import dash_bootstrap_components as dbc
from running_graphics import buildAvgHRGraph, buildDistanceGraph, buildAerGraph

register_page(
    __name__,  # calling page objects' self.name
    name="Running",  # your own selected name of the page
    top_nav=True,
    path="/running",  # path to the page on the website
)

avgHRGraph = buildAvgHRGraph()
distanceGraph = buildDistanceGraph()
aer_graph = buildAerGraph()


# dash.page_container gives this page back to app.py
def layout():
    layout = html.Div(
        children=[
            html.Div(
                children=[
                    # html.Img(src="assets/police.jpg",
                    # alt="Logo of the Belgian police force", height = 200, width = 200),
                    html.Br(),
                    html.Br(),
                    html.H2(children="Беговая аналитика", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    dbc.Col(
                        children=[
                            dbc.Row(children=avgHRGraph, className="running_graphs "),
                            dbc.Row(
                                children=distanceGraph, className="running_graphs "
                            ),
                            dbc.Row(children=aer_graph, className="running_graphs "),
                        ]
                    ),
                ],
                className="home-page-logo-text",
            )
        ],
        className="page-content-home",
    )
    return layout
