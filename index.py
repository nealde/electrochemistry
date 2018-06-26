import base64
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from textwrap import dedent

from app import app
from apps import home, chapter1

#mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'
#app.scripts.append_script({ 'external_url' : mathjax })
app.css.append_css({'external_url':
                    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

## load katex
#app.css.append_css({'external_url':
#                    "https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css"})

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
# reference for adding left / center / inline latex math

#app.layout = html.Div(id='main',children=[
#  html.P(children='Delicious \(\pi\) is inline with my goals.'),
#  html.P(children='$$ \lim_{t \\rightarrow \infty} \pi = 0$$'),
#  html.P(style={'text-align':'left'}, children='\(\\leftarrow \pi\)'),
#  html.P(style={'text-align':'left'}, children='not much left.'),
#  html.P(style={'text-align':'right'},children='\(\pi \\rightarrow\)'),
#  html.P(style={'text-align':'right'},children='but it feels so right.'),
#])

# to add a new page, create a new file in /apps
# then, add a reference in the callback at the bottom of this page and tie it into a
# dcc.Link with the desired text

home = html.Div([
    html.H1('Welcome to the ECS @ UW Supplement to "Electrochemical Methods" by Allen J. Bard and Larry R. Faulkner.'),

    html.P('''The aim of this application is to aid in explaining the theory discussed,
        and to help to improve understanding
        of electrochemical systems through the use of interactive visualizations.'''),
    html.Div([html.Img(src='https://images-na.ssl-images-amazon.com/images/I/41RJ7v13PgL._SX327_BO1,204,203,200_.jpg')]),
    html.H3('A list of chapters is available below:'),
    dcc.Link('Chapter 1 - Introduction', href='/Chapter1'),
    html.P('Chapter 2'),
    html.P('Chapter 3'),
    html.P('Chapter 4'),
    html.P('Chapter 5'),
    html.P('Chapter 6'),
    html.P('Chapter 7'),
    html.P('Chapter 8'),

   html.P(
        '''
        This page was created and is maintained by the Neal Dawson-Elli and members of the
        Student Chapter of the Electrochemical Society at the University of Washington.'''),
    html.Div([
    html.Img(src='https://github.com/nealde/electrochemistry/raw/master/Logo_ECSatUW.png'),
    ],
    style={
        'minHeight':'100px',
        'vertical-align': 'middle'},
    ),

], style={'justify-content':'center',
         'textAlign':'center'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Chapter1':
         return chapter1.layout
    elif pathname == '/': # main page
        return home
    else:
        return 404

if __name__ == '__main__':
    app.run_server(debug=True)
