import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home, app1, app2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

home = html.Div([
    dcc.Markdown("welcome home!   $$ frac{5}{\alpha} $$"),
    dcc.Markdown('''

        # This is an <h1> tag

        ## This is an <h2> tag

        ###### This is an <h6> tag
        ''')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    elif pathname == '/home':
        print("ok")
        return home.layout
    else:
        return home

if __name__ == '__main__':
    app.run_server(debug=True)
