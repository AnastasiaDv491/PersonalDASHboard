from dash import (
    html,
    register_page,
)  # , callback # If you need callbacks, import it here.
import dash_bootstrap_components as dbc


register_page(
    __name__,  # calling page objects' self.name
    name="Home",  # your own selected name of the page
    top_nav=True,
    path="/",  # path to the page on the website
)

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Спортивная Аналитика", className="card-title"),
            dbc.Button("перейти", color="primary", href="/sports"),
        ]
    )
)
second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Беговая Аналитика", className="card-title"),
            dbc.Button("перейти", color="primary", href="/running"),
        ]
    )
)
cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=4),
    ],
    className="home_page_button_container",
)


# dash.page_container gives this page back to app.py
def layout():
    layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.Br(),
                    html.Br(),
                    html.H2("Дэшборд спортивной аналитики.", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.P("Цели разработки данного дэшборда:"),
                    html.Ul(
                        children=[
                            html.Li(
                                "Визуализация спортивных данных используя разные форматы и срезы информации."
                            ),
                            html.Li(
                                "Выявление зависимости между заданными параметрами."
                            ),
                            html.Li(
                                "Оценка спортивного и физического развития с целью корректировки физической нагрузки."
                            ),
                        ]
                    ),
                    html.H4("Данные"),
                    html.P(
                        "Данные для дэшборда были подтянуты из приложения Garmin Connect, где фиксировались спортивные показатели. В дэшборде используется временной интервал с 2020 по 2024 год. Это интервал, когда пользователь носил часы Garmin."
                    ),
                    cards,
                ],
                className="home-page-logo-text",
            )
        ],
        className="page-content-home",
    )
    return layout
