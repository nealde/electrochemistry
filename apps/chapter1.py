import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from textwrap import dedent
import numpy as np
import base64

from app import app

# import all the images
img1 = base64.b64encode(open('CH1/fig_1_2_3.png', 'rb').read())
img2 = base64.b64encode(open('CH1/fig_1_2_5.png', 'rb').read())

# set lists for dropdowns
s1 = ['step','ramp','triangle']

layout = html.Div([
    dcc.Markdown(dedent('''
    ### Table of Contents:
  * [Chapter 1.2](#chapter-2) Double Layer Capacitance
  * [Chapter 1.3](#chapter-3) Fardaic Processes
  * [Chapter 1.4](#chapter-4) Modes of Mass Transfer
  * [Chapter 1.5](#chapter-5) Nernstian Reactions with Coupled Chemical Reactions
  ''')),

    html.H3('Chapter 1.2 - Double Layer Capacitance'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(img1.decode())),
    ],
    style={
        'minHeight':'100px',
        'vertical-align': 'middle'},
    ),
    html.Div([
        html.P('''
        Double layer capacitance is a phenomenon which occurs on the surface of charged conductive materials immersed in electrolyte.
        In essence, different boundaries can be drawn which indicate what phenomena occur.
        '''),
        html.P('''
        The responses of this system can be modeled mathematically.
        '''),
        dcc.Markdown(dedent('''
        The relationship between a **voltage step** and the *response current* is given by:
        $$i = \\frac{E}{R_s}e^{(-t/(R_sC_d))}$$

        The **charge stored** during this event can be represented by the following:
        $$q = EC_d(1-e^{(-t/(R_sC_d))})$$

        ''')),
        html.Img(src='data:image/png;base64,{}'.format(img2.decode()))
    ], style={'width':'80%'}),
    dcc.Dropdown(
        id='graph1-input',
        options=[{'label': s, 'value': i} for i,s in enumerate(s1)],
        value = 0,
    ),
    html.Div(id='graphs'),
    html.Div([
        html.Div(children=['E (applied voltage): 0.5 Volts'],id='g1_E_label'),
        dcc.Slider(id = 'g1_E', max=3, min=0, step=0.01, updatemode='drag', value=0.5, marks = {0: 0, 3: 3}),
        html.P('Rs (resistance): 1 Ohms', id='g1_Rs_label'),
        dcc.Slider(id = 'g1_Rs', max=3, min=0.01, step=0.01, updatemode='drag', value=1, marks = {0: 0.01, 3: 3}),
        html.P('Cd (interface capacitance): 20 Farads', id='g1_Rs_label'),
        dcc.Slider(id = 'g1_Cd', max=60, min=0.01, step=0.01, updatemode='drag', value=20, marks = {0: 0.01, 60: 60})

    ])
], className='container')

@app.callback(Output('graphs','children'),
             [Input('graph1-input','value'),Input('g1_E','value'),Input('g1_Rs','value'),Input('g1_Cd','value')])
def update_Graph1(dropdown, E, Rs, Cd):
#    print(dropdown)
    x = np.linspace(1e-5, 60, 200)

    if dropdown == 0: # step
        y1 = x*E*1/x
        y2 = E/Rs*np.exp(-x/(Rs*Cd))
    elif dropdown == 1: # ramp
        y1 = (E*x)/max(x)
        v=E/max(x)
        y2 = v*Cd*(1-np.exp(-x/(Rs*Cd)))
    elif dropdown == 2: # triangle
        y1 = np.concatenate((((2*E*x)/max(x))[:len(x)//2-1], (2*E-(2*E*x)/max(x))[len(x)//2:len(x)-1]), axis=0)
        v=E/max(x)
        y2 = np.concatenate(((v*Cd*(1-np.exp(-x/(Rs*Cd))))[0:len(x)//2-1],(-v*Cd*(1-np.exp(-x/(Rs*Cd))))[0:len(x)//2-1]),axis=0)
    data1 = [{'x': x,
           'y' : y1,
           'type': 'scatter', 'mode':'lines'}]
    data2 = [{'x': x,
           'y' : y2,
           'type': 'scatter', 'mode':'lines'}]
#    print(data)
    return [html.H5('Applied E (Volts)'),
            dcc.Graph(
            id = 'graph1',
                figure={
                    'data': data1,
                    'layout': {
                        'margin': {'b': 0, 'r': 10, 'l': 60, 't': 0},
                        'height' : 200,
                        'yaxis' : {'range':[-1.5,4.5]}
                    }
                }
            ),
           html.H5('Resultant i (Amps)'),
            dcc.Graph(
            id = 'graph2',
                figure={
                    'data': data2,
                    'layout': {
                        'margin': {'b': 60, 'r': 10, 'l': 60, 't': 0},
                        'height' : 200,
                        'yaxis' : {'range':[-2,4.5]},
                        'xaxis' : {'title':'Time (s)'}
                    }
                }
            ),
           ]

@app.callback(Output('g1_E_label','children'),[Input('g1_E','value')])
def update_E1(value):
    return 'E (applied voltage): {} Volts'.format(str(value))

@app.callback(Output('g1_Rs_label','children'),[Input('g1_Rs','value')])
def update_E1(value):
    return 'Rs (resistance): {} Ohms'.format(str(value))

@app.callback(Output('g1_Cd_label','children'),[Input('g1_Cd','value')])
def update_E1(value):
    return 'Cd (interface capacitance): {} Farads'.format(str(value))

