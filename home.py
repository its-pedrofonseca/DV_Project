import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import plotly.graph_objects as go
import dash_core_components as dcc


F1_TEAMS = "https://simracingsetup.com/wp-content/uploads/2020/02/F1-2020-All-Team-Desktop-Wallpaper.jpg"

def table_drivers():
    fig = go.Figure(data=[go.Table(header=dict(values=['Position', 'Team', 'Code', 'Name', 'Points']),
                                   cells=dict(values=[
                                       ['1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º', '11º', '12º',
                                        '13º', '14º', '15º', '16º', '17º', '18º', '19º', '20º', '21º', '22º', '23º'],
                                       ['Mercedes', 'Mercedes', 'Red Bull', 'Racing Point', 'Renault', 'McLaren',
                                        'Red Bull', 'Ferrari', 'McLaren', 'Racing Point', 'AlphaTauri', 'Renault',
                                        'Ferrari', 'AlphaTauri', 'Racing Point', 'Alfa Romeo', 'Alfa Romeo', 'Williams',
                                        'Haas F1 Team', 'Haas F1 Team', 'Williams', 'Haas F1 Team', 'Williams'],
                                       ['HAM', 'BOT', 'VER', 'PER', 'RIC', 'SAI', 'ALB', 'LEC', 'NOR', 'STR', 'GAS',
                                        'OCO', 'VET', 'KVY', 'HUL', 'RAI', 'GIO', 'RUS', 'GRO', 'KEV', 'LAT', 'FIT',
                                        'AIT'],
                                       ['Lewis Hamilton', 'Valtteri Bottas', 'Max Verstappen', 'Sergio Pérez',
                                        'Daniel Ricciardo', 'Carlos Sainz', 'Alexander Albon', 'Charles Leclerc',
                                        'Lando Norris', 'Lance Stroll', 'Pierre Gasly', 'Esteban Ocon',
                                        'Sebastian Vettel', 'Daniil Kvyat', 'Nico Hülkenberg', 'Kimi Räikkönen',
                                        'Antonio Giovinazzi', 'George Russell', 'Romain Grosjean', 'Kevin Magnussen',
                                        'Nicholas Latifi', 'Pietro Fittipaldi', 'Jack Aitken'],
                                       [347, 223, 214, 125, 119, 105, 105, 98, 97, 75, 75, 62, 33, 32, 10, 4, 4, 3, 2,
                                        1, 0, 0, 0]]))
                          ])
    return fig


def table_cons():
    fig = go.Figure(data=[go.Table(header=dict(values=['Position', 'Team', 'Points']),
                                   cells=dict(values=[['1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º'],
                                                      ['Mercedes', 'Red Bull', 'McLaren', 'Racing Point', 'Renault',
                                                       'Ferrari', 'AlphaTauri', 'Alfa Romeo', 'Haas F1 Team',
                                                       'Williams'],
                                                      [573, 319, 202, 195, 181, 131, 107, 8, 3, 0]
                                                      ])),
                          ])
    return fig

layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Home', className="text-left")
                ],width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H5('The 2020 FIA Formula One World Championship was the motor racing championship for Formula One cars '
            'which marked the 70th anniversary of the first Formula One World Drivers Championship.'
            ' The championship was recognised by the governing body of international motorsport,'
            ' the Fédération Internationale de Automobile (FIA), as the highest class of competition'
            ' for open-wheel racing cars. Drivers and teams competed for the titles of World Drivers'
            ' Champion and World Constructors Champion respectively.', className="mx-2 my-2")
                ],width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H5('The championship was originally due to start in March, but the start was postponed until'
        ' July in response to the COVID-19 pandemic. The season was due to be contested over a record of'
        ' 22 Grands Prix, but as some races were cancelled and new races were added to replace them, a total of'
        ' 17 races were run. The season started in July with the Austrian Grand Prix and ended in December'
        ' with the Abu Dhabi Grand Prix. Lewis Hamilton and Mercedes entered the season as the reigning World Drivers '
        'and World Constructors champions respectively, after they both won their sixth championship in 2019.'
        ' At the Emilia Romagna Grand Prix, Mercedes secured their seventh consecutive Constructors Championship '
        'making them the only team to win seven consecutive championships, breaking Ferrari record from 1999 to 2004.',
                            className="mx-2 my-2")
                ],width=12)
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.H4('2020 Drivers Final Standings', className="text-center")
                ], width={'size': 6}),
                dbc.Col([
                    html.H4('2020 Constructors Final Standings', className="text-center")
                ], width={'size': 6})
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(figure=table_drivers()), body=True, color="#31343b"
                    )
                ],width={'size':6}),
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(figure=table_cons()), body=True, color="#31343b"
                    )
                ],width={'size':6})
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H5('The F1 grid is composed by 10 Teams that compete every year with each other trying to get the best '
                            'classification possible. Each Team is composed by two Drivers, making a total of 20 drivers per race.'
                            ' Nevertheless, there can be some replacements throughout the season in case of serious crashes or due to '
                            'illness. In 2020, there was a total of 23 drivers.', className="mx-2 my-2")
                ],width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("55.404s", className="text-center"),
                            html.H3("Fastest Lap in 2020 - George Russel, Sakhir", className="text-center"),
                        ])
                    ], body=True, color="#31343b")
                ], width={'size': 3}, className='my-2'),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("1.86s", className="text-center"),
                            html.H3("Fastest Pit Stop in 2020 - Red Bull, Portimao", className="text-center"),
                        ])
                    ], body=True, color="#31343b")
                ], width={'size': 3}, className='my-2'),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("336.7km/h", className="text-center"),
                            html.H3("Fastest Speed in 2020 - Ferrari, Barcelona", className="text-center"),
                        ])
                    ], body=True, color="#31343b")
                ], width={'size': 3}, className='my-2'),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("7 Titles", className="text-center"),
                            html.H3("Lewis Hamilton - 7th World Champion Title", className="text-center"),
                        ])
                    ], body=True, color="#31343b")
                ], width={'size': 3}, className='my-2'),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardImg(src="/assets/logos_horizontal.png", top=True),
                    )
                ], width=12)
            ],className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H6('Datasets: https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020', className="text-left")
                ],width=6),
                dbc.Col([
                    html.H6('Members: Frederico Rodrigues - m2020583, Gonçalo Carvalho - m2020664, Pedro Fonseca - m20201037', className="text-right")
                ],width=6)
            ]),
    ], fluid=True)