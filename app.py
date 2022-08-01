# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('time-series-starter-dataset.zip')
df.dropna(subset=['Sales_quantity'], inplace=True)

fig = go.Figure(data=[go.Scatter(x=df['Period'], y=df['Sales_quantity'])])

app.layout = html.Div([
    html.H1(id='title', children='Sales Quantity in Time'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=False)
