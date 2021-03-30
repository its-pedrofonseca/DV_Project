import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objs as go
import app
F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

# Dataset Processing

path = 'datasets/f1_2020_drivers.xlsx'
df = pd.read_excel(path)


driver_options = [
    dict(label='Driver' + driver, value=driver)
    for driver in df['surname'].unique()]


dropdown_driver = dcc.Dropdown(
        id='driver_drop',
        options=driver_options,
        value=['bottas'],
        multi=True
    )

layout = html.Div([

    html.H1('Drivers'),
    html.H4('Choose the drivers that you want to compare'),
    html.Div([
        html.Div([
            dropdown_driver,
            html.Br(),

        ], style={'width': '20%'}, className=''),

        html.Div([
            dcc.Graph(id='graph_example')
        ], style={'width': '80%'}, className='box')
    ], style={'display': 'flex'}),
])


@app.app.callback(
    Output('graph_example', 'figure'),
    Input('driver_drop', 'value')

)
def update_graph(driver):

    scatter_data = []

    for drive in driver:
        df2 = df.loc[df['surname'] == drive]

        temp_data = dict(
            type='scatter',
            y=df2['Pointsinday'],
            x=df2['date'],
            name=drive
        )

        scatter_data.append(temp_data)

    scatter_layout = dict(xaxis=dict(title='RaceDate'),
                          yaxis=dict(title='Pointsinday')
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)

    return fig