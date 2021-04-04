import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objs as go
from plotly.graph_objs import Figure
import plotly.express as px

import app

F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

# Dataset Processing

path = 'datasets/f1_2020_constructors.xlsx'
df = pd.read_excel(path)

df_constructors = pd.read_csv('datasets/f1_2020_constructors.csv', error_bad_lines=False)
df_drivers = pd.read_csv('datasets/f1_2020_drivers_fred.csv', error_bad_lines=False)

df_drivers2 = pd.read_csv('datasets/f1_2020_constructors.csv', error_bad_lines=False)

df_drivers['date'] = pd.to_datetime(df_drivers['date'])
df_drivers = df_drivers.sort_values(by='date')
pistas = df_drivers.name_x.unique()

fl = df_drivers[['name_x', 'fastestLapTime', 'surname', 'Team']]
pistas_fl = fl.groupby('name_x', as_index=False)['fastestLapTime'].min()

driver = []
for time in pistas_fl.fastestLapTime:
    driver.append(fl.loc[fl['fastestLapTime'] == time, 'surname'])

Constructor = ['Mercedes', 'Renault', 'McLaren', 'Red Bull', 'Renault', 'Red Bull', 'Red Bull',
               'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'Mercedes', 'McLaren',
               'McLaren', 'Mercedes']
pistas_fl = pistas_fl.assign(Constructor=Constructor)
pistas_fl

champion_time = fl.loc[fl['Team'] == 'Mercedes'].groupby('name_x', as_index=False)['fastestLapTime'].min()
champion_time = champion_time.fastestLapTime
champion_time

def selected_constructor_diff(constructor):
    time_per_race = fl.loc[fl['Team'] == constructor].groupby('name_x', as_index=False)['fastestLapTime'].min()
    time_per_race = time_per_race.fastestLapTime
    time_diffc = pd.DataFrame(champion_time.subtract(time_per_race))
    time_diffc['color']=['red' if val<0 else 'lawngreen' for val in time_diffc.fastestLapTime]
    time_diffc['Time Difference (s)'] = time_diffc['fastestLapTime']
    return time_diffc

team_radio = dcc.RadioItems(
    id='radio-items',
    options=[
        {'label': 'Renault ', 'value': 'Renault'},
        {'label': 'Alfa Romeo ', 'value': 'Alfa Romeo'},
        {'label': 'Red Bull ', 'value': 'Red Bull'},
        {'label': 'AlphaTauri ', 'value': 'AlphaTauri'},
        {'label': 'Williams Racing ', 'value': 'Williams Racing'},
        {'label': 'McLaren ', 'value': 'McLaren'},
        {'label': 'Ferrari ', 'value': 'Ferrari'},
        {'label': 'Haas ', 'value': 'Haas'},
        {'label': 'Racing Point ', 'value': 'Racing Point'},
    ],
    value='McLaren', labelStyle={'display': 'inline-block'},
    inputStyle={"margin-right": "3px", "margin-left": "70px", },
    persistence=True,
    persistence_type='session',
)

team_options = [
    dict(label=' ' + team, value=team)
    for team in df['name_y'].unique()]

dropdown_team = dcc.Dropdown(
    id='team_drop',
    options=team_options,
    value=['Mercedes', 'Red Bull'],
    multi=True,
    persistence=True,
    persistence_type='session'
)

layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Constructors', className="text-left")
                ],width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4('Choose the Constructors to compare:', className="text-left")
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dropdown_team,
                ], width={'size':12})
            ]),
            dbc.Row([
                dbc.Col([
                    html.H5('Cumulative Points per Race', className="text-center")
                ],width=6),
                dbc.Col([
                    html.H5('Constructors Rank per Race', className="text-center")
                ],width=6)
            ],className="mt-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_Constructors', style={'height': 570}),
                        body=True, color="#31343b"
                    )
                ],width={'size':6}, className='my-2'),
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_Constructors2', style={'height': 570}),
                        body=True, color="#31343b"
                    )
                ], width={'size': 6}, className='my-2'),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H6()
                ], width=6),
                dbc.Col([
                    html.H6()
                ], width=6)
            ], className="mt-2 mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H5('Fastest Lap Time Difference to Championship Winning Team', className="text-center")
                ], width=12),
            ], className="mt-2"),
            dbc.Row([
                dbc.Col([
                    html.Div(team_radio, className="text-center"),
                ], width={'size':12}),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(id='graph_time', style={'height':570}),
                        body=True, color="#31343b"
                    )
                ],width={'size':12})
            ], className="mb-2"),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardImg(src="/assets/logos_horizontal.png", top=True),
            )
        ], width=12)
    ], className="mb-2"),



], fluid=True)

@app.app.callback(
    Output('graph_Constructors', 'figure'),
    Input('team_drop', 'value')
)
def update_graph(team):
    scatter_data = []
    for tea in team:
        df_s = df.loc[df['name_y'] == tea]
        temp_data = dict(
            type='scatter',
            y=df_s['points'],
            x=df_s['name_x'],
            name=tea
        )
        scatter_data.append(temp_data)
    scatter_layout = dict(xaxis=dict(title='Race', showgrid=False),
                          yaxis=dict(title='Points', showgrid=False),
                          paper_bgcolor='rgba(255,255,255)',
                          plot_bgcolor='rgba(0,0,0,0)'
                          )
    fig3 = go.Figure(data=scatter_data, layout=scatter_layout)
    fig3.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig3.update_yaxes(showline=True, linewidth=1, linecolor='black')
    return fig3

@app.app.callback(
    Output('graph_Constructors2', 'figure'),
    Input('team_drop', 'value')
)
def update_graph2(team):
    scatter_data = []
    for tea in team:
        df_s = df.loc[df['name_y'] == tea]
        temp_data = dict(
            type='scatter',
            y=df_s['position'],
            x=df_s['name_x'],
            name=tea
        )
        scatter_data.append(temp_data)
    scatter_layout = dict(xaxis=dict(title='Race', showgrid=False),
                          yaxis=dict(title='Constructors Rank', showgrid=False),
                          paper_bgcolor='rgba(255,255,255)',
                          plot_bgcolor='rgba(0,0,0,0)'
                          )
    fig4 = go.Figure(data=scatter_data, layout=scatter_layout)
    fig4.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig4.update_yaxes(showline=True, linewidth=1, linecolor='black',  autorange="reversed")
    return fig4

pistas = df_drivers2["name_x"].unique()

@app.app.callback(
    Output('graph_time', 'figure'),
    Input('radio-items', 'value')
)
def graph2(team):
    fig2 = px.bar(selected_constructor_diff(team),
                  x=pistas,
                  y='Time Difference (s)',
                  color='color',
                  color_discrete_sequence=selected_constructor_diff(team).color.unique(),
                  )
    fig2.update_traces(showlegend = False)
    fig2.update_layout(barmode='stack',paper_bgcolor='rgba(255,255,255)',plot_bgcolor='rgba(0,0,0,0)',xaxis_title="Race",
    yaxis_title="Time Difference in Seconds")
    fig2.update_yaxes(gridcolor='black', showgrid=True, gridwidth=0.5)

    return fig2