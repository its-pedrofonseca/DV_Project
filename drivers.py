import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objs as go
from plotly.graph_objs import Figure

import app
F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

# Dataset Processing

path = 'datasets/f1_2020_drivers.xlsx'
df = pd.read_excel(path)

df_constructors = pd.read_csv('datasets/f1_2020_constructors.csv', error_bad_lines=False)
df_drivers = pd.read_csv('datasets/f1_2020_drivers_fred.csv', error_bad_lines=False)

df_drivers['date'] = pd.to_datetime(df_drivers['date'])
df_drivers = df_drivers.sort_values(by='date')
pistas = df_drivers.name_x.unique()

fl = df_drivers[['name_x', 'fastestLapTime', 'surname', 'Team']]
pistas_fl = fl.groupby('name_x', as_index=False)['fastestLapTime'].min()

driver = []
for time in pistas_fl.fastestLapTime:
    driver.append(fl.loc[fl['fastestLapTime'] == time, 'surname'])

Driver = ['Hamilton', 'Ricciardo', 'Norris', 'Verstappen', 'Ricciardo', 'Verstappen', 'Verstappen',
          'Hamilton', 'Hamilton', 'Hamilton', 'Hamilton', 'Bottas', 'Russell', 'Bottas', 'Sainz',
          'Norris', 'Hamilton']

pistas_fl = pistas_fl.assign(Driver=Driver)

fl = fl.sort_values('name_x')

def selected_driver(name):
    times = fl.loc[fl['surname'] == name, 'fastestLapTime'].reset_index(drop=True)
    return times


def selected_driver_diff(name):
    time = fl.loc[fl['surname'] == name, 'fastestLapTime'].reset_index(drop=True)
    time_diff = time.subtract(pistas_fl['fastestLapTime'])
    return time_diff

driver_radio = dcc.RadioItems(
    id='radio-items',
    options=[
        {'label': 'Ocon ', 'value': 'Ocon'},
        {'label': 'Räikkönen ', 'value': 'Räikkönen'},
        {'label': 'Albon ', 'value': 'Albon'},
        {'label': 'Hamilton ', 'value': 'Hamilton'},
        {'label': 'Gasly ', 'value': 'Gasly'},
        {'label': 'Latifi ', 'value': 'Latifi'},
        {'label': 'Sainz ', 'value': 'Sainz'},
        {'label': 'Vettel ', 'value': 'Vettel'},
        {'label': 'Giovinazzi ', 'value': 'Giovinazzi'},
        {'label': 'Norris ', 'value': 'Norris'},
        {'label': 'Russell ', 'value': 'Russell'},
        {'label': 'Magnussen ', 'value': 'Magnussen'},
        {'label': 'Grosjean ', 'value': 'Grosjean'},
        {'label': 'Leclerc ', 'value': 'Leclerc'},
        {'label': 'Stroll ', 'value': 'Stroll'},
        {'label': 'Ricciardo ', 'value': 'Ricciardo'},
        {'label': 'Bottas ', 'value': 'Bottas'},
        {'label': 'Verstappen ', 'value': 'Verstappen'},
        {'label': 'Kvyat ', 'value': 'Kvyat'},
        {'label': 'Hülkenberg ', 'value': 'Hülkenberg'},
        {'label': 'Fittipaldi ', 'value': 'Fittipaldi'},
        {'label': 'Pérez ', 'value': 'Pérez'},
        {'label': 'Aitken ', 'value': 'Aitken'}
    ],
    value='Ocon', labelStyle={'display': 'inline-block'},
    inputStyle={"margin-right": "2px", "margin-left": "12px"},
    persistence=True,
    persistence_type='session'
)

driver_options = [
    dict(label=' ' + driver, value=driver)
    for driver in df['surname'].unique()]


dropdown_driver = dcc.Dropdown(
        id='driver_drop',
        options=driver_options,
        value=['Bottas', 'Vettel'],
        multi=True,
        persistence=True,
        persistence_type='session'
    )


layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Drivers', className="text-left")
                ],width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4('Choose the drivers to compare:', className="text-left")
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dropdown_driver,
                ], width={'size':12})
            ]),
            dbc.Row([
                dbc.Col([
                    html.H5('Cumulative Points per Race', className="text-center")
                ],width=6),
                dbc.Col([
                    html.H5('Final Position per Race', className="text-center")
                ],width=6)
            ],className="mt-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_pointsperrace', style={'height':570}),
                        body=True, color="#31343b"
                    )
                ],width={'size':6}, className='my-2'),
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_rank', style={'height': 570}),
                        body=True, color="#31343b"
                    )
                ], width={'size': 6}, className='my-2'),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H6("* if the Driver didn't participate in the race, no information will be presented", className="text-center")
                ], width=6),
                dbc.Col([
                    html.H6('* if rank=0, then the Driver Did Not Finished (DNF)', className="text-center")
                ], width=6)
            ], className="mt-2 mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H5('Lap Time Difference in seconds between selected Driver and Fastest Lap', className="text-center")
                ],width=12),
            ],className="mt-2"),
            dbc.Row([
                dbc.Col([
                    html.Div(driver_radio, className="text-center"),
                ], width={'size':12})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_timedelta', style={'height':570}),
                        body=True, color="#31343b"
                    )
                ],width={'size':12})
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H6('* if time=200s then the Driver DNF (Did Not Finished)'
                            ' or was declassified by the 107% rule.', className="text-left"),
                ], width=12),
            ], className="mt-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardImg(src="/assets/logos_horizontal.png", top=True),
                    )
                ], width=12)
            ], className="mb-2"),

    ], fluid=True)


@app.app.callback(
    Output('graph_pointsperrace', 'figure'),
    Input('driver_drop', 'value')
)
def update_graph(driver):
    scatter_data = []

    for drive in driver:
        df_s = df.loc[df['surname'] == drive]
        temp_data = dict(
            type='scatter',
            y=df_s['Pointsinday'],
            x=df_s['name_x'],
            name=drive
        )
        scatter_data.append(temp_data)
    scatter_layout = dict(xaxis=dict(title='Race'),
                          yaxis=dict(title='Points'),
                          paper_bgcolor='rgba(255,255,255)',
                          plot_bgcolor='rgba(0,0,0,0)'
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='black')
    return fig

@app.app.callback(
    Output('graph_rank', 'figure'),
    Input('driver_drop', 'value')
)
def update_graph2(driver):
    scatter_data = []

    for drive in driver:
        df_s = df.loc[df['surname'] == drive]
        temp_data = dict(
            type='scatter',
            y=df_s['rank'],
            x=df_s['name_x'],
            name=drive
        )
        scatter_data.append(temp_data)
    scatter_layout = dict(xaxis=dict(title='Race'),
                          yaxis=dict(title='Drivers Ranks'),
                          paper_bgcolor='rgba(255,255,255)',
                          plot_bgcolor='rgba(0,0,0,0)'
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='black', autorange="reversed")
    return fig

@app.app.callback(
    Output('graph_timedelta', 'figure'),
    Input('radio-items', 'value')
)
def graph2(driver):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=pistas_fl.name_x.unique(),
        x=pistas_fl['fastestLapTime'],
        name='Fastest Lap Recorded',
        orientation='h',
        marker=dict(
            color='rgba(255, 0, 0, 0.7)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=pistas_fl.name_x.unique(),
        x=selected_driver_diff(driver),
        name=driver,
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        ),
    ))
    fig.update_layout(barmode='stack',paper_bgcolor='rgba(255,255,255)',plot_bgcolor='rgba(0,0,0,0)', xaxis_title="Fastest Lap Time in Seconds",
    yaxis_title="Race")
    fig.update_xaxes( gridcolor='black', showgrid=True, gridwidth=0.5)

    return fig