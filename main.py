import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import io
import requests

# Read file

path = 'datasets/f1_2020_drivers.csv'
df = pd.read_csv(path, error_bad_lines=False)

# Interactive Components

races_options = [dict(label=races, value=races) for races in df['raceId'].unique()]

races_options = [
    {'label': 'Austrian GP', 'value': 'Austrian GP'},
    {'label': 'Styrian  GP', 'value': 'Styrian  GP'},
    {'label': 'Hungarian GP', 'value': 'Hungarian GP'},
    {'label': 'British GP', 'value': 'British GP'},
    {'label': '70th Anniversary GP', 'value': '70th Anniversary GP'},
    {'label': 'Spanish GP', 'value': 'Spanish GP'},
    {'label': 'Belgian GP', 'value': 'Belgian GP'},
    {'label': 'Italian GP', 'value': 'Italian GP'},
    {'label': 'Tuscan GP', 'value': 'Tuscan GP'},
    {'label': 'Russian GP', 'value': 'Russian GP'},
    {'label': 'Eifel GP', 'value': 'Eifel GP'},
    {'label': 'Portuguese GP', 'value': 'Portuguese GP'},
    {'label': 'Emilia Romagna GP', 'value': 'Emilia Romagna GP'},
    {'label': 'Turkish GP', 'value': 'Turkish GP'},
    {'label': 'Bahrain GP', 'value': 'Bahrain GP'},
    {'label': 'Sakhir GP', 'value': 'Sakhir GP'},
    {'label': 'Abu Dhabi GP', 'value': 'Abu Dhabi GP'}
]

nav = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="logo.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Logo", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

# APP

app = dash.Dash(__name__)

server = app.server

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    nav
)

if __name__ == '__main__':
    app.run_server(debug=True)

