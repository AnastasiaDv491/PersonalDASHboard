from dash import (
    html,
    register_page,
)  # , callback # If you need callbacks, import it here.

import dash_bootstrap_components as dbc
from content_creation.running_graphics import (
    buildAvgHRGraph,
    buildDistanceGraph,
    buildAerGraph,
)

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
                    html.Br(),
                    html.Br(),
                    html.H2(children="Беговая аналитика", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    html.P(
                        "В данном разделе представлена беговая статистика. Задача: определить прогресс беговых тренировок с целью их дальнейшей корректировки для разработки программы подготовки к Московскому марафону 2025."
                    ),
                    html.Br(),
                    html.Ol(
                        children=[
                            html.Li(
                                [
                                    html.P(
                                        "На первом графике представлена эволюция среднего сердечного ритма, начиная с 2020 года. Считается, что кардио-нагрузка со временем понижает сердечный ритм, так как физическая форма спортсмена с тренировками становится лучше. Исходя из графика, мы не можем сказать, что сердечный ритм сильно упал. Динамика графика стабильная и сердечный ритм держится в районе 160-170 ударов в минуту. Это говорит о слабом спортивном прогрессе."
                                    ),
                                    html.B("Возможные корректировки: "),
                                    html.P(
                                        "Усилить количество кардио-тренировок; добавить продолжительные по времени забеги в медленном темпе."
                                    ),
                                ]
                            ),
                            html.Li(
                                [
                                    html.P(
                                        "На втором графике представлена динамика изменения величины беговой дистанции. Чем больше мы бегаем и тренируемся, тем лучше становится выносливость и мы можем бежать дольше и дальше. Исходя из графика, мы можем сказать, что со временем дистанция увеличилась, что говорит о прогрессе в беге."
                                    ),
                                    html.B("Возможные корректировки: "),
                                    html.P("Комбинировать короткие и длинные забеги."),
                                ]
                            ),
                            html.Li(
                                [
                                    html.P(
                                        "На третьем графике представлен средний аэробный обмен. Аэробный обмен показывает эффективность тренировки. Он делится на 6 зон: 0 - 0.9 Нет эффекта; 1 - 1.9 Слабый эффект; 2-2.9 Поддерживающий эффект; 3-3.9 Развивающий эффект; 4-4.9 Высокий развивающий эффект и 5-5.9 Перегрузка. Исходя из данных графика, можно сделать вывод, что большая часть беговых тренировок находится в поддерживающей зоне. Это неплохо, но может объяснить медленный беговой прогресс."
                                    ),
                                    html.B("Возможные корректировки: "),
                                    html.P(
                                        "Включить в спортивную программу тренировки в зоне 4 (Развивающей) и 5 (Высоко развивающей)."
                                    ),
                                ]
                            ),
                        ]
                    ),
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
