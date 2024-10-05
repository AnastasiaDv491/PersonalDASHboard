from dash import (
    html,
    register_page,
)  # , callback # If you need callbacks, import it here.
from sports_graphics import (
    create_pie_chart,
    buildYearFilter,
    buildYearGraph,
    buildSeasonGraph,
    buildSeasonFilter,
    buildMap,
)
import dash_bootstrap_components as dbc


# import dash_dangerously_set_inner_html
graph1 = buildYearGraph()
yearFilter = buildYearFilter()


graph2 = buildSeasonGraph()
seasonFilter = buildSeasonFilter()

map = buildMap()

register_page(
    __name__,  # calling page objects' self.name
    name="Спорт",  # your own selected name of the page
    top_nav=True,
    path="/sports",  # path to the page on the website
)


# dash.page_container gives this page back to app.py
def layout():
    layout = html.Div(
        children=[
            html.Div(
                children=[
                    # html.Img(
                    #     # src="assets/police.jpg",
                    #     alt="Logo of the Belgian police force",
                    #     height=200,
                    #     width=200,
                    # ),
                    html.Br(),
                    html.Br(),
                    html.H2(children="Спортивная Аналитика", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ullamcorper purus non commodo consequat. Nam nec accumsan nibh, vitae congue odio. Duis eu eleifend lacus. Quisque interdum neque ut feugiat feugiat. Curabitur ac tortor enim. Nulla sagittis porttitor laoreet. Nullam ex leo, egestas a varius ac, suscipit ac mi. Praesent malesuada dolor non massa convallis, et fringilla purus ornare. Duis accumsan lorem vel dolor eleifend finibus. Aliquam scelerisque felis sed felis molestie volutpat in id velit. Ut vulputate nisi lorem, in efficitur eros ultricies nec. Nulla nunc augue, rutrum sit amet consequat eu, interdum a felis. Pellentesque enim erat, cursus vel nisl sit amet, facilisis scelerisque eros."
                    ),
                    html.Hr(),
                    html.Br(),
                    html.H2(children="Статистика", className="graph_header2"),
                    html.Div(
                        children=[
                            html.Ul(
                                id="my-list",
                                children=[
                                    html.Li("Thids is an item"),
                                    html.Li("Thids is an item"),
                                    html.Li("Thids is an item"),
                                ],
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H3("Статистика 1"),
                                        yearFilter,
                                        graph1,
                                    ],
                                    className="pie_graph_container",
                                    style={"display": "inline-block"},
                                ),
                            ),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H3("Статистика 2"),
                                        seasonFilter,
                                        graph2,
                                    ],
                                    className="pie_graph_container",
                                    style={"display": "inline-block"},
                                ),
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(children=[html.H3("Места активностей: ")])
                            ),
                            map,
                        ]
                    ),
                ],
                className="home-page-logo-text",
            )
        ],
        className="page-content-home",
    )
    return layout
