from dash import html
import dash_bootstrap_components as dbc


# Icons: https://fontawesome.com/search
def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            html.Div(
                children=[
                    dbc.NavItem(
                        children=[
                            dbc.NavLink(
                                [
                                    html.I(
                                        className="fa-brands fa-github"
                                    ),  # Font Awesome Icon
                                    "Github",  # Text beside icon
                                ],
                                href="https://github.com/AnastasiaDv491/PersonalDASHboard",
                                target="_blank",
                            ),
                        ]
                    ),
                ]
            ),
            html.Div(
                children=[
                    dbc.NavbarBrand("Домой", href="/"),
                    dbc.NavbarBrand("Спорт", href="/sports"),
                    dbc.NavbarBrand("Бег", href="/running"),
                ]
            ),
        ]
    )

    return navbar
