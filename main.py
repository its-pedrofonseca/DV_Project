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

path = 'C:/Users/Pedro/Desktop/Data Visualization Project/2-entrega/F1/races_2020.csv'
df = pd.read_csv(path, error_bad_lines=False)

# Interactive Components

races_options = [dict(label=races, value=races) for races in df['raceId'].unique()]

slider_races = dcc.Slider(
        id='slider_races',
        min=0,
        max=len(df['name']) -1,
        marks={0:"Austrian GP", 1:"Styrian  GP", 2:"Hungarian GP",
               3:"British GP", 4:"70th Anniversary GP", 5:"Spanish GP",
               6:"Belgian GP", 7:"Italian GP", 8:"Tuscan GP", 9:"Russian GP",
               10:"Eifel GP", 11:"Portuguese GP", 12:"Emilia Romagna GP",
               13:"Turkish GP", 14:"Bahrain GP", 15:"Sakhir GP",
               16:"Abu Dhabi GP"},
        step=1
    )

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

# Callbacks
@app.callback(
    Output('graph_example', 'figure'),
    [Input('slider_races', 'value')]
)# Graphic
def update_graph(races, gas, year):
    filtered_by_year_df = df[(df['year'] >= year[0]) & (df['year'] <= year[1])]

    scatter_data = []

    for race in races:
        filtered_by_year_and_country_df = filtered_by_year_df.loc[filtered_by_year_df['country_name'] == country]

        temp_data = dict(
            type='scatter',
            y=filtered_by_year_and_country_df[gas],
            x=filtered_by_year_and_country_df['year'],
            name=race
        )

        scatter_data.append(temp_data)

    scatter_layout = dict(xaxis=dict(title='Year'),
                          yaxis=dict(title=gas)
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

