import dash
import dash_bootstrap_components as dbc

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server