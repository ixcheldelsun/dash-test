from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import numpy as np

import dash

dash.register_page(__name__, path_template="/predictions/<id_fi>")

# def layout(id_fi=None):
    
#     df = pd.read_csv('time-series-starter-dataset.zip')
#     df.dropna(subset=['Sales_quantity'], inplace=True)

#     fig = go.Figure(data=[go.Scatter(x=df['Period'], y=df['Sales_quantity'])])
    
#     return html.Div([
#     html.H1(id='title', children=f'{id_fi}'),
#     dcc.Graph(figure=fig)
# ])

def layout(id_fi=None, **other_unknown_query_strings):
    #df = pd.read_csv('time-series-starter-dataset.zip')
    #df.dropna(subset=['Sales_quantity'], inplace=True)

    #fig = go.Figure(data=[go.Scatter(x=df['Period'], y=df['Sales_quantity'])])
    #import pdb; pdb.set_trace()
    
    

    return html.Div(
	children=[
        dcc.Location(id='url', refresh=False),
	    html.H1(id='title', children='El id es: {}'.format(id_fi)),
        dcc.Graph(id='scatter')

	])
    
@callback(Output('scatter', 'figure'),
              [Input('url', 'pathname')])
def display_page(pathname):
    id_fi = pathname.split('/')[-1]
    np.random.seed(int(id_fi)) 
    
    random_x= np.random.randint(1,101,100) 
    random_y= np.random.randint(1,101,100) 
        
    
    fig = px.scatter(random_x, random_y)
    return fig

