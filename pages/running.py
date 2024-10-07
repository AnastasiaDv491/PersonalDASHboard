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
                    html.Br(),
                    html.Br(),
                    html.H2(children="Беговая аналитика", className="graph_header"),
                    html.Br(),
                    html.Br(),
                    html.Hr(),
                    html.P(
                        "В данном разделе представлена беговая статистика. Задачей является определить прогресс беговых тренировок с целью их дальнейшей корректировки для создания программы к подготовки к Московскому марафону 2025. "
                    ),
                    html.Br(),
                    html.Ol(
                        children=[
                            html.Li(
                                [
                                    html.P(
                                        "В первом графике представлена эволюция среднего сердечного ритма с 2020 года. Кардио нагрузка со временем понижает сердечный ритм, так как физическая форма спортсмена с тренировками становится лучше. Исходя из графика, мы не можем сказать, что сердечный ритм сильно упал. Динамика графика стабильная и сердечный ритм держится в районе 160-170 ударов в минуту. Это говорит о плохом спортивном прогрессе . "
                                    ),
                                    html.B("Возможные корректировки: "),
                                    html.P(
                                        "Усилить количество кардио тренировок; добавить долгие забеги на медленном темпе."
                                    ),
                                ]
                            ),
                            html.Li(
                                [
                                    html.P(
                                        "Во втором графике представлена динамика развития беговой дистанции. Чем больше мы бегаем и тренируемся, тем лучше становится выносливость и мы можем бежать дольше и дальше. Исходя из графика, мы можем сказать, что со временем дистанция увеличилась, что говорит о прогрессе в беге."
                                    ),
                                    html.B("Возможные корректировки: "),
                                    html.P("Комбинировать короткие и длинные забеги."),
                                ]
                            ),
                            html.Li(
                                [
                                    html.P(
                                        "В третьем графике представлен средний аэробный обмен. Аэробный обмен показывает эффективность тренировки. Он делится на 6 зон: 0 - 0.9 Нет эффекта; 1 - 1.9 Слабый эффект; 2-2.9 Поддерживающий эффект; 3-3.9 Развивающий эффект; 4-4.9 Высокий развивающий эффект и 5-5.9 Перенагруз. Большая часть беговых тренировок находится в поддерживающей зоне. Это не плохо, но может объяснить медленный беговой прогресс. "
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
