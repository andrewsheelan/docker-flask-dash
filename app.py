from flask import Flask
from flask import request, render_template
from config import BaseConfig

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

server = Flask(__name__)
server.config.from_object(BaseConfig)
@server.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


# the style arguments for the plots ,datatable.
chart_style = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# the Header
header=html.Div(dbc.Row(dbc.Label("DashBoard" ,color="white",width=12,style={"height":"25" ,"background-color": "lightseagreen"})))
# the Sidebar
sidebar = dbc.Nav(
    [
        dbc.NavLink("Take me Home", active=True, href="/", external_link=True),
        dbc.NavLink("Graph 1", href="#example-graph"),
        dbc.NavLink("Graph 2", href="#example-graph-2"),
        dbc.NavLink("Scatter plot", href="#scatterplot"),
    ]
)
content = html.Div(id="page-content", style=CONTENT_STYLE)

# Plots
graph=html.Div(
    html.Div([

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Bar graph'
                }
            }
        ),

    ])
)
# Line graph
mynew=dcc.Graph(
            id='example-graph-2',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 9, 8], 'type': 'line', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Line Graph'
                }
            }
        )
np.random.seed(42)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)

scat=html.Div([
    dcc.Graph(id='scatterplot', figure={
        'data':[
            go.Scatter(
                x=random_x,
                y=random_y,
                mode='markers'
            )],
        'layout':go.Layout(title='Scatter plot',xaxis={'title': 'Product'},
                           yaxis={'title': 'Sales'})

    })
])
app.layout = html.Div([dcc.Location(id="url"),header,sidebar,content, mynew, scat])

if __name__ == '__main__':
    app.run_server(debug=True)
