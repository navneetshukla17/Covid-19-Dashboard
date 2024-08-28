import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-KyZXEAg3QhqLMpG8r+Knujsl5/WTdOihzJjibJxy1zqD4wDibL0c5o49yIf6Yyoi',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Corona Virus Pandemic', style={'color':'#fff', 'text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', style={'color':'#fff'}, className='text-light'),
                    html.H4('600', style={'color':'#fff'}, className='text-light')
                ], className='card-body')
            ], className='card bg-danger') 
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', style={'color':'#fff'}, className='text-light'),
                    html.H4('600', style={'color':'#fff'}, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', style={'color':'#fff'}, className='text-light'),
                    html.H4('600', style={'color':'#fff'}, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', style={'color':'#fff'}, className='text-light'),
                    html.H4('600', style={'color':'#fff'}, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')], className='col-md-3')
    ], className='row'),
    html.Div([
        html.Div([], className='col-md-6'),
        html.Div([], className='col-md-6')
    ], className='row'),
    html.Div([
        html.Div([], className='col-md-12')
    ], className='row'),
], className='container')



if __name__=='__main__':
    app.run(debug=True)
    
    