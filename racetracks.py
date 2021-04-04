import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

from app import app

path = 'datasets/f1_2020_drivers.xlsx'
df = pd.read_excel(path)

F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

colorscale = [[0, 'rgb(255,0,0)'], [1, 'rgb(255,0,0)']]


def map(df):
    df_racetracks = df[['raceId', 'name_x', 'lat', "lng", "name_y", "location", "country"]].drop_duplicates("raceId")
    df_racetracks["color"] = 0

    l = ['Valtteri Bottas, Lewis Hamilton',
         'Valtteri Bottas, Lewis Hamilton',
         'Lewis Hamilton',
         'Lewis Hamilton, Max Verstappen',
         'Lewis Hamilton, Max Verstappen',
         'Lewis Hamilton',
         'Lewis Hamilton',
         'Pierre Gasly',
         'Lewis Hamilton',
         'Valtteri Bottas',
         'Lewis Hamilton',
         'Lewis Hamilton',
         'Lewis Hamilton',
         'Lewis Hamilton',
         'Lewis Hamilton, Sergio Perez',
         'Lewis Hamilton, Sergio Perez',
         'Max Verstappen'
         ]

    l1 = ['Mercedes',
         'Mercedes',
         'Mercedes',
         'Mercedes, Red Bull Racing Honda',
         'Mercedes, Red Bull Racing Honda',
         'Mercedes',
         'Mercedes',
         'AlphaTauri Honda',
         'Mercedes',
         'Mercedes',
         'Mercedes',
         'Mercedes',
         'Mercedes',
         'Mercedes',
         'Mercedes, Racing Point BWT Mercedes',
         'Mercedes, Racing Point BWT Mercedes',
         'Max Verstappen'
         ]

    df_racetracks = df_racetracks.sort_values(by=['raceId'])

    df_racetracks["winner"] = l
    df_racetracks["winner_cons"] = l1


    data_scattergeo = dict(type='scattergeo',
                           lat=df_racetracks['lat'],
                           lon=df_racetracks['lng'],
                           #text=df_racetracks['name_y'],
                           mode=['markers', 'lines', 'text'][0],
                           hovertemplate=#'Grand Prix: ' + df_racetracks["name_x"] + '<br>'+
                                         'Racetrack: ' + df_racetracks["name_y"] + '<br>'+
                                         'Location: ' + df_racetracks["location"] + '<br>'+
                                         'Country: ' + df_racetracks["country"] + '<br>'+
                                         '*Winner Driver(s): ' + df_racetracks["winner"] + '<br>'
                                         '*Winner Constructor(s): ' + df_racetracks["winner_cons"] + '<br>'
                           '<extra></extra>',

                           marker=dict(color='red', size=12)
                           )


    layout_scattergeo = dict(geo=dict(scope='world',
                                      projection=dict(type='equirectangular'
                                                      ),
                                      showocean=True,
                                      oceancolor='azure',
                                      bgcolor='#f9f9f9',
                                      ),

                             title=dict(
                                 text='',
                                 x=.5
                             ),
                             paper_bgcolor='#ffffff',
                             margin=dict(t=0, l=0, r=0, b=0)
                             )

    choropleth = go.Figure(data=data_scattergeo, layout=layout_scattergeo)

    return choropleth


layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Racetracks', className="text-left")
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4('Hover above track locations to get more information:', className="text-left")
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dcc.Graph(figure=map(df), style={'height':580}),
                        body=True, color="#31343b"
                    )
                ],width={'size':12}, className='my-2'),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    html.H6('* Due to COVID-19 some tracks were repeated and in some locations'
                            ' there may be more than one winner', className="text-center")
                ], width=12)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardImg(src="/assets/logos_horizontal.png", top=True),
                    )
                ], width=12)
            ], className="mb-2"),

], fluid=True)
