import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

F1_TEAMS = "https://simracingsetup.com/wp-content/uploads/2020/02/F1-2020-All-Team-Desktop-Wallpaper.jpg"

layout = html.Div([
    html.H1('Home Page'),
    html.Br(),
    html.Br(),

    html.H5('The 2020 FIA Formula One World Championship was the motor racing championship for Formula One cars '
            'which marked the 70th anniversary of the first Formula One World Drivers Championship.'
            ' The championship was recognised by the governing body of international motorsport,'
            ' the Fédération Internationale de Automobile (FIA), as the highest class of competition'
            ' for open-wheel racing cars. Drivers and teams competed for the titles of World Drivers'
            ' Champion and World Constructors Champion respectively.'),
    html.Br(),
    html.H5('The championship was originally due to start in March, but the start was postponed until'
        ' July in response to the COVID-19 pandemic. The season was due to be contested over a record of'
        ' 22 Grands Prix, but as some races were cancelled and new races were added to replace them, a total of'
        ' 17 races were run. The season started in July with the Austrian Grand Prix and ended in December'
        ' with the Abu Dhabi Grand Prix. Lewis Hamilton and Mercedes entered the season as the reigning World Drivers'
        'and World Constructors champions respectively, after they both won their sixth championship in 2019.'
        ' At the Emilia Romagna Grand Prix, Mercedes secured their seventh consecutive Constructors Championship '
        'making them the only team to win seven consecutive championships, breaking Ferrari record from 1999 to 2004.'
            ),
    html.Br(),

])