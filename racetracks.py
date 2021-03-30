import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly.express as px
from dash.exceptions import PreventUpdate

path = 'datasets/f1_2020_drivers.csv'
df = pd.read_csv(path, error_bad_lines=False)

df_racetracks = df[['lat', "lng", "name_y", "location", "country"]]

app = dash.Dash(__name__)

F1_LOGO = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png"

app.layout = html.Div([
    html.H1('Racetracks'),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        dcc.Input(id='input_state', type='number', inputMode='numeric', value=2007,
                  max=2007, min=1952, step=5, required=True),
        html.Button(id='submit_button', n_clicks=0, children='Submit'),
        html.Div(id='output_state'),
    ], style={'text-align': 'center'})
])

@app.callback(
    [
        Output("bar_graph", "figure"),
        Output("choropleth", "figure"),
        Output("aggregate_graph", "figure"),
    ],
    [
        Input("year_slider", "value"),
        Input("country_drop", "value"),
        Input("gas_option", "value"),
        Input("lin_log", "value"),
        Input("projection", "value"),
        Input('sector_option', 'value')
    ]
)
def plots(year, countries, gas, scale, projection, sector):
    ############################################First Bar Plot##########################################################
    data_bar = []
    for country in countries:
        df_bar = df.loc[(df['country_name'] == country)]

        x_bar = df_bar['year']
        y_bar = df_bar[gas]

        data_bar.append(dict(type='bar', x=x_bar, y=y_bar, name=country))

    layout_bar = dict(title=dict(text='Emissions from 1990 until 2015'),
                      yaxis=dict(title='Emissions', type=['linear', 'log'][scale]),
                      paper_bgcolor='#f9f9f9'
                      )

    #############################################Second Choropleth######################################################

    df_emission_0 = df.loc[df['year'] == year]

    z = np.log(df_emission_0[gas])

    data_choropleth = dict(type='choropleth',
                           locations=df_emission_0['country_name'],
                           # There are three ways to 'merge' your data with the data pre embedded in the map
                           locationmode='country names',
                           z=z,
                           text=df_emission_0['country_name'],
                           colorscale='inferno',
                           colorbar=dict(title=str(gas.replace('_', ' ')) + ' (log scaled)'),

                           hovertemplate='Country: %{text} <br>' + str(gas.replace('_', ' ')) + ': %{z}',
                           name=''
                           )

    layout_choropleth = dict(geo=dict(scope='world',  # default
                                      projection=dict(type=['equirectangular', 'orthographic'][projection]
                                                      ),
                                      # showland=True,   # default = True
                                      landcolor='black',
                                      lakecolor='white',
                                      showocean=True,  # default = False
                                      oceancolor='azure',
                                      bgcolor='#f9f9f9'
                                      ),

                             title=dict(
                                 text='World ' + str(gas.replace('_', ' ')) + ' Choropleth Map on the year ' + str(
                                     year),
                                 x=.5  # Title relative position according to the xaxis, range (0,1)

                             ),
                             paper_bgcolor='#f9f9f9'
                             )

    ############################################Third Scatter Plot######################################################

    df_loc = df.loc[df['country_name'].isin(countries)].groupby('year').sum().reset_index()

    data_agg = []

    for place in sector:
        data_agg.append(dict(type='scatter',
                             x=df_loc['year'].unique(),
                             y=df_loc[place],
                             name=place.replace('_', ' '),
                             mode='markers'
                             )
                        )

    layout_agg = dict(title=dict(text='Aggregate CO2 Emissions by Sector'),
                      yaxis=dict(title=['CO2 Emissions', 'CO2 Emissions (log scaled)'][scale],
                                 type=['linear', 'log'][scale]),
                      xaxis=dict(title='Year'),
                      paper_bgcolor='#f9f9f9'
                      )

    return go.Figure(data=data_bar, layout=layout_bar), \
           go.Figure(data=data_choropleth, layout=layout_choropleth), \
           go.Figure(data=data_agg, layout=layout_agg)



if __name__ == '__main__':
    app.run_server(debug=True)