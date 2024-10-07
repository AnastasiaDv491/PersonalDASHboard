from dash import (
    html,
    register_page,
)  # , callback # If you need callbacks, import it here.
from content_creation.sports_graphics import (
    buildYearFilter,
    buildYearGraph,
    buildSeasonGraph,
    buildSeasonFilter,
    buildMap,
    buildQuickFacts,
)
import dash_bootstrap_components as dbc


graph1 = buildYearGraph()
yearFilter = buildYearFilter()


graph2 = buildSeasonGraph()
seasonFilter = buildSeasonFilter()

map = buildMap()
quickFacts = buildQuickFacts()

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
                    html.Br(),
                    html.Br(),
                    html.H2(children="Спортивная Аналитика", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    html.P(
                        "В данном разделе представлена общая спортивная статистика. Здесь мы знакомимся с данными, их динамикой и проводим аналитический анализ. В первой части представлены быстрые факты о беговых и силовых тренировок, так как они являются наиболее частыми в моем спортивном досуге. Также, представлена карта всех мест бега и выбран топ-3 локации, исходя из частоты беговых тренировок."
                    ),
                    html.Hr(),
                    html.Br(),
                    dbc.Row(
                        [
                            dbc.Col(html.Div(children=[html.H3("Места бега"), map])),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H3("Немного фактов за 2020-2024: "),
                                        quickFacts,
                                    ]
                                )
                            ),
                        ]
                    ),
                    html.Hr(),
                    html.H2(children="Статистика", className="graph_header2"),
                    html.P("Перед анализом были построенны следующие гипотезы: "),
                    html.Div(
                        children=[
                            html.Ul(
                                id="my-list",
                                children=[
                                    html.Li(
                                        "1. Разнообразие спортивных активностей увеличивается с течением времени."
                                    ),
                                    html.Li(
                                        "2. Наиболее активные периоды активности - это лето и весна."
                                    ),
                                    html.Li(
                                        "3. Со временем, силовые тренировки занимают большую часть спортивного досуга."
                                    ),
                                ],
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H3("Анализ активностей по году"),
                                        html.P(
                                            "С 2020 по 2024 год наблюдается эволюция в тренировках. Если изначально бег составлял большую часть физической нагрузки, то с 2022 года большее внимание стало уделяться силовым тренировкам. Это подтверждает гипотезу №3. В период с 2023 по 2024 год процент силовых тренировок незначительно снижается, что связано с тренировками к полу-марафону, который состоялся в мае 2024 года."
                                        ),
                                        yearFilter,
                                        graph1,
                                    ],
                                    className="pie_graph_container",
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                    },
                                ),
                            ),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H3("Аналих сезонности активностей"),
                                        html.P(
                                            "Многие спортивные активности поддаются влиянию сезонов. Например, летом бывает жарко и бегать на улице невыносимо. New York Times назвали осень самым благоприятным сезоном для бега. Исходя из полученных данных, мы видим, что, действительно, процент беговых тренировок летом и зимой самый низкий, но пик активности был весной, а не осенью. Это может быть связано с большой загруженностью в начале учебного года. Таким образом, гипотеза №2 опровегнута. Также, стоит заметить, что весной возможно самое большое разнообразие тренировок (например, йога, бассейн)."
                                        ),  # https://www.nytimes.com/2023/09/28/well/move/fall-running-training.html
                                        seasonFilter,
                                        graph2,
                                    ],
                                    className="pie_graph_container",
                                    style={"display": "inline-block"},
                                ),
                            ),
                        ]
                    ),
                ],
                className="home-page-logo-text",
            )
        ],
        className="page-content-home",
    )
    return layout
