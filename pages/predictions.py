from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import numpy as np
from urllib.parse import urlparse, parse_qs
import dash

dash.register_page(__name__, path_template="/predictions")

# def layout(id_fi=None):
    
#     df = pd.read_csv('time-series-starter-dataset.zip')
#     df.dropna(subset=['Sales_quantity'], inplace=True)

#     fig = go.Figure(data=[go.Scatter(x=df['Period'], y=df['Sales_quantity'])])
    
#     return html.Div([
#     html.H1(id='title', children=f'{id_fi}'),
#     dcc.Graph(figure=fig)
# ])

def layout(id_fi=None):
    #df = pd.read_csv('time-series-starter-dataset.zip')
    #df.dropna(subset=['Sales_quantity'], inplace=True)

    #fig = go.Figure(data=[go.Scatter(x=df['Period'], y=df['Sales_quantity'])])
    
    
    

    return html.Div(
	children=[
        dcc.Location(id='url', refresh=False),
	    html.H1(id='title', children='El id es: {}'.format(id_fi)),
        dcc.Graph(id='scatter')

	])
    
@callback(Output('scatter', 'figure'),
              [Input('url', 'href')])
def display_page(href:str):
    parsed_url = urlparse(href)
    np.random.seed(int(parse_qs(parsed_url.query)["id_fi"][0])) 
    
    random_x= np.random.randint(1,101,100) 
    random_y= np.random.randint(1,101,100) 
        
    
    fig = px.scatter(random_x, random_y)
    return fig

