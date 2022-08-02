# -*- coding: utf-8 -*-
from dash import Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

#from pages import predictions

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

server = app.server


if __name__ == '__main__':
	app.run_server(debug=True)
