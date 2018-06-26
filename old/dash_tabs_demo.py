import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from loremipsum import get_sentences

app = dash.Dash()

app.scripts.config.serve_locally = True


app.config.suppress_callback_exceptions = True

labels = ['Introduction','Reactions','Electrochemistry','Physics']
app.layout = html.Div([
    dcc.Tabs(
        tabs=[
            {'label': 'Chapter {} - {}'.format(i,labels[i-1]), 'value': i} for i in range(1, 5)
        ],
        value=3,
        id='tabs'
    ),
    html.Div(id='tab-output'),
    html.Div([dcc.Graph(id='graph'),
#    dcc.Slider(
#            id='year-slider',
#            min=1,
#            max=10,
#            value=5,
#            step=0.01
##            marks={'%i':i for i in range(1,10)}
#
#        )
             ])
], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})

x = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
y1 = [219, 146, 112, 127, 124, 180, 236, 207, 236, 263, 350, 430, 474, 526, 488, 537, 500, 439]
y2 = [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270, 299, 340, 403, 549, 499]

@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_content(value):
    data = [
        {
            'x': x,
            'y': y1,
            'name': 'Rest of world',
            'marker': {
                'color': 'rgb(55, 83, 109)'
            },
            'type': ['bar', 'scatter', 'box'][int(value) % 3]
        },
        {
            'x': x,
            'y': y2,
            'name': 'China',
            'marker': {
                'color': 'rgb(26, 118, 255)'
            },
            'type': ['bar', 'scatter', 'box'][int(value) % 3]
        }
    ]
#    @app.callback(Output('graph','data'),[Input('year-slider','value')],[State('graph','data')])
#    def update_graph(value, data):
#        print(value)
#        print(data)
#        return data
    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        ),
        dcc.Slider(
            id='year-slider',
            min=1,
            max=10,
            value=5,
            step=0.01
#            marks={'%i':i for i in range(1,10)}

        )
#        html.Div(' '.join(get_sentences(10)))
    ])
@app.callback(Output('tab-output', 'children'), [Input('year-slider', 'value')],[State('graph','data'),State('tabs','value')])
def update_graphs(slider_value, data, value):
    print(slider_value)
    print(data)
    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        ),
        dcc.Slider(
            id='year-slider',
            min=1,
            max=10,
            value=5,
            step=0.01
#            marks={'%i':i for i in range(1,10)}

        )
#        html.Div(' '.join(get_sentences(10)))
    ])
#    return [
#        {
#            'x': x,
#            'y': [y*slider_value for y in y1],
#            'name': 'Rest of world',
#            'marker': {
#                'color': 'rgb(55, 83, 109)'
#            },
#            'type': ['bar', 'scatter', 'box'][int(value) % 3]
#        },
#        {
#            'x': x,
#            'y': y2,
#            'name': 'China',
#            'marker': {
#                'color': 'rgb(26, 118, 255)'
#            },
#            'type': ['bar', 'scatter', 'box'][int(value) % 3]
#        }
#    ]


if __name__ == '__main__':
    app.run_server(debug=True)
