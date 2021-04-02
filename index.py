import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import constructors

# Connect to main app.py file
from app import app

# Connect to your app pages
import racetracks
import drivers
import constructors
import home

F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

nav_item_home = dbc.NavItem(dbc.NavLink("Home", href="/home", active="exact"))
nav_item_drivers = dbc.NavItem(dbc.NavLink("Drivers", href="/drivers", active="exact"))
nav_item_constructors = dbc.NavItem(dbc.NavLink("Constructors", href="/constructors", active="exact"))
nav_item_racetracks = dbc.NavItem(dbc.NavLink("Racetracks", href="/racetracks", active="exact"))

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        #dbc.Col(dbc.NavbarBrand("F1-2020", className="ml-2")),
                        dbc.Col(html.Img(src=F1_LOGO, height="30px", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://www.formula1.com/",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item_home, nav_item_drivers, nav_item_constructors, nav_item_racetracks], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],fluid=True
    ),
    color="#31343b",
    dark=True,
    className="mb-3",
)

content = html.Div(id="page-content")

app.layout = html.Div(
    [dcc.Location(id="url"), logo, content],
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    if pathname == "/home":
        return home.layout
    elif pathname == "/drivers":
        return drivers.layout
    elif pathname == "/constructors":
        return constructors.layout
    elif pathname == "/racetracks":
        return racetracks.layout
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)