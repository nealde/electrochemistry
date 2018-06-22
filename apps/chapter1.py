import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from textwrap import dedent
import numpy as np
import base64
import os

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CH1')

from app import app
# import all the images

img1 = base64.b64encode(open('CH1/fig_1_2_3.png', 'rb').read())
img2 = base64.b64encode(open('CH1/fig_1_2_5.png', 'rb').read())
img3 = base64.b64encode(open('CH1/fig_1_3_5.png', 'rb').read())
img4 = base64.b64encode(open('CH1/fig_1_3_6.png', 'rb').read())
#img5 = base64.b64encode(open('CH1/fig_1_3_10.png', 'rb').read())
#img6 = base64.b64encode(open('CH1/fig_1_3_12.png', 'rb').read())
#img7 = base64.b64encode(open('CH1/fig_1_4_1.png', 'rb').read())
#img8 = base64.b64encode(open('CH1/fig_1_4_4.png', 'rb').read())
#img9 = base64.b64encode(open('CH1/fig_1_5_1.png', 'rb').read())


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
        dcc.Slider(id = 'g1_E', max=3, min=0, step=0.01, updatemode='drag', value=2.5, marks = {0.01: 0, 3: 3}),
        html.P('Rs (resistance): 1 Ohms', id='g1_Rs_label'),
        dcc.Slider(id = 'g1_Rs', max=3, min=0, step=0.01, updatemode='drag', value=1, marks = {0.01: 0, 3: 3}),
        html.P('Cd (interface capacitance): 20 Farads', id='g1_Cd_label'),
        dcc.Slider(id = 'g1_Cd', max=60, min=0, step=0.01, updatemode='drag', value=20, marks = {0.01: 0, 60: 60})

    ], style= {'textAlign': 'center'}),
    html.Div([
    dcc.Markdown(dedent('''


    ### Chapter 1.3 - Faradaic Processes
    ##### Galvanic cells - Reactions occur spontaneously at the electrodes when connected by a conductor.
    * Primary and secondary batteries
    * Fuel cells

    ##### Electrolytic cells - Reactions are effected by the applied voltage moreso than the open Circuit Potential (OCP)
    * Electrolytic synthesis
    * Electroplating
    * Electrorefining (like copper)

    The function of a half-cell is independent of galvanic or eletrolytic status.
    **Reduction** occurs at the cathode, **oxidation** occurs at the anode.

    The equilibrium potential is an important reference point of the system.
    * Cell potential changing from equilibrium is called *polarization*
    * Extent of polarization is measured by overpotential
    $$ \eta = E - E_{eq} $$

    ''')),
#    html.Div([
#        html.P('hello $$ \eta = E - E_{eq} $$'),
##        html.Img(src='data:image/png;base64,{}'.format(img1.decode())),
#    ]),
#    html.Div([
#    html.Img(src='data:image/png;base64,{}'.format(img1.decode()))
#    ],
#    style={
#        'minHeight':'100px',
#        'vertical-align': 'middle'},
#    ),
#    html.P(children='Delicious \(\pi\) is inline with my goals.'),
    dcc.Markdown(dedent('''

    ##### Factors affecting electrode reaction rate and current
    1. Mass transfer
    2. Electron transfer at electrode surface
    3. Chemical reactions before / after electron transfer
    4. Other surface reactions, like adsorption, desorption, or crystallization
    *rate constants may be dependent upon potential*
    **Overpotential** is the sum of terms associated with each step - *mass transfer overpotential*, *charge-transfer overpotential*, etc
    $$ E_{applied} = E_{cd}-iR_s=E_{eq,cd}+\eta-iR_s $$
    The above indicates that the *overpotential* and *bulk soluion resistance* should be counted separately''')),

    dcc.Markdown(dedent('''
    ### Chapter 1.4 - Modes of Mass Transfer
    If an eelctrode process has fast, heterogeneous charge-transfer kinetics and mobile, reversible homogeneous equations:
    1. The homogeneous reactions can be regarded as being at equilibrium
    2. the *surface concentrations* are related to the electrode potential by an equation of the Nernst form, meaning that the reaction is sufficiently fast as to be mass-transfer limited. $$v_{rxn} = v_{mt}=\\frac{i}{nFA}$$

    ##### 3 modes of mass transfer:
    1. Migration - Movement of a charged body under the influence of an electric field (a gradient of electrical potential).
    2. Diffusion - Movement of a species under the influence of a gradient of chemical potential (i.e. a concentration gradient).
    3. Convection - Stirring or hydrodynamic transport. Generally, fluid flow occurs because of natual convection (convection caused by density gradients) and forced convection, and may be characterized by stagnant regions, laminar flow, and turbulent flow.

    Mass transfer to an electrode is governed by the *Nernst-Planck equation (1D)*
    $$J_{i}(x) = -D_{i}\\frac{\partial C_i(x) }{\partial x}-\\frac{z_iF}{RT}D_iC_i\\frac{\partial \phi (x) }{\partial x} +C_iv(x)$$

    The transport of C to the electrode is mass-transfer limited, such that the diffusion layer thickness is always constant as long as D is constant.

    $$ \\frac{i}{nFA}=m_O[C^*_O-C_O(x=0)] $$

    $$ i_l=nFAm_OC^*_O $$

    **When R is not present:** $$E = E_{1/2} = E^{0'}-\\frac{RT}{nF}ln\\frac{m_O}{m_R}$$
    $$ E = E_{1/2} +\\frac{RT}{nF} ln\\frac{i_l-i}{i} $$

    **When R present:** $$ E = E^{0'}-\\frac{RT}{nF}ln\\frac{m_O}{m_R}+\\frac{RT}{nF}ln(\\frac{i_{l,c}-i}{i-i_{l,a}}) $$

    **When R is insoluble (like with metal plating)**

    $$E = E^{0'}-\\frac{RT}{nF}lnC^*_O+\\frac{RT}{nF}ln(\\frac{i_l-i}{i})$$

    $$i = i_l, \eta_{conc} \\rightarrow \\infty$$

    ''')),
#    dcc.Markdown(dedent('''
    html.H3('Chapter 1.5 - Nernstian Reactions with Coupled Chemical Reactions'),
    html.P('''
    $$E = E^{0'} + \\frac{RT}{nF}ln\frac{m_R+\mu k}{m_O}+\\frac{RT}{nF}ln(\\frac{i_l-i}{i}) $$

    $$ E = E_{1/2}' + \\frac{0.059}{n}ln\\frac{m_R+\mu k}{m_O} $$

    $$ m_R=0.62D_R^{2/3}v^{-1/6}\omega ^{1/2} $$'''),
    html.H5('Unperturbed equation:'),
    html.P("$$ E'_{1/2} = E_{1/2} + \\frac{0.059}{n}ln\\frac{\mu k}{m_R} $$"),
    html.H5('Rotating equation:'),
    html.P("$$ E'_{1/2} = E_{1/2} + \\frac{0.059}{n}ln\\frac{\mu k}{0.62D_R^{2/3}v^{-1/6}} - \\frac{0.059}{n}ln \omega $$"),



    html.Img(src='data:image/png;base64,{}'.format(img4.decode())),
#
#    dcc.Markdown(dedent('''
#    ##### 3-electrode cells for measuring electrochemical cell resistance''')),
#    html.Div([
#    html.Img(src='data:image/png;base64,{}'.format(img5.decode()), style={'width':'70%'}),
#    html.Img(src='data:image/png;base64,{}'.format(img6.decode()), style={'width':'70%'}),
#    html.Img(src='data:image/png;base64,{}'.format(img7.decode()), style={'width':'70%'}),
#    ]),
    ]),
    html.Div(id='graphs_disk'),
    html.Div([
        html.Div(children=['E (applied voltage): 0.5 Volts'],id='g2_E_label'),
        dcc.Slider(id = 'g2_E', max=3, min=0, step=0.01, updatemode='drag', value=0.5, marks = {0.01: 0, 3: 3}),

        html.P('il 60 ', id='g2_il_label'),
        dcc.Slider(id = 'g2_il', max=60, min=0, step=0.01, updatemode='drag', value=50, marks = {0.01: 0, 3: 3}),

        html.P('n 0.01 ', id='g2_n_label'),
        dcc.Slider(id = 'g2_n', max=.2, min=0, step=0.01, updatemode='drag', value=.08, marks = {0.01: 0, 3: 3}),

        html.P('u 0.01 ', id='g2_u_label'),
        dcc.Slider(id = 'g2_u', max=1, min=0, step=0.01, updatemode='drag', value=.01, marks = {0.01: 0, 3: 3}),

        html.P('k 1', id='g2_k_label'),
        dcc.Slider(id = 'g2_k', max=2, min=0, step=0.01, updatemode='drag', value=1, marks = {0.01: 0, 3: 3}),

        html.P('mR 0.5', id='g2_mR_label'),
        dcc.Slider(id = 'g2_mR', max=1, min=0, step=0.01, updatemode='drag', value=.5, marks = {0.01: 0, 3: 3}),

        html.P('DR 0.02', id='g2_DR_label'),
        dcc.Slider(id = 'g2_DR', max=.8, min=0, step=0.01, updatemode='drag', value=.02, marks = {0.01: 0, .8: .8}),

        html.P('v 0.3', id='g2_v_label'),
        dcc.Slider(id = 'g2_v', max=.8, min=0, step=0.01, updatemode='drag', value=.3, marks = {0.01: 0, .8: .8}),

        html.P('\(\omega\) 3', id='g2_w_label'),
        dcc.Slider(id = 'g2_w', max=60, min=0, step=0.01, updatemode='drag', value=3, marks = {0.01: 0, 60: 60})

    ], style= {'textAlign': 'center'}),

], className='container')



# callbacks

# graph 1
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

# graph 2
# list of elements
l1 = ['E','il','n','u','k','mR','DR','v','w']
label_list = ['']

@app.callback(Output('graphs_disk','children'),
             [Input('g2_{}'.format(i),'value') for i in l1])
def update_Graph1(E,il,n,u,k,mR,DR,v,w):

    x = np.linspace(1e-5, 50, 200)
    E_half = E

    E_half_1 = E_half+0.059/n*np.log(u*k/mR)
    E_half_2 = E_half+0.059/n*np.log(u*k/(0.62*DR**(2/3)*v**(-1/6)))-0.059/n*np.log(w)
#    w=6
    w *= 2
    E_half_3 = E_half+0.059/n*np.log(u*k/(0.62*DR**(2/3)*v**(-1/6)))-0.059/n*np.log(w)
    y = E_half_1 + 0.059/n*np.log((il-x)/x) # E values
    y2 = E_half_2 + 0.059/n*np.log((il-x)/x)
    y3 = E_half_3 + 0.059/n*np.log((il-x)/x)
##    data = go.Scatter(x=x, y=y, mode='lines')
##    print(data)
#    print(x,y)
    data1 = [{'x': x,
           'y': y,
           'type': 'scatter', 'mode':'lines', 'name':'Static Electrode'},
            {'x': x,
           'y': y2,
           'type': 'scatter', 'mode':'lines', 'name':'Rotating Electrode'},
            {'x': x,
           'y': y3,
           'type': 'scatter', 'mode':'lines', 'name':'2x Rotating Electrode'}]

    return [html.H5('Rotating Disk Electrode'),
        dcc.Graph(
            id = 'graph_rot_disk',
                figure={
                    'data': data1,
                    'layout': {
                        'margin': {'b': 60, 'r': 10, 'l': 60, 't': 0},
                        'height' : 400,
                        'yaxis' : {'range':[-5,5.5]},
#                        'xaxis' : {'title':'Time (s)'}
                    }
                }
            ),
           ]

