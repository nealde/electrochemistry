#import dash
#import dash_html_components as html
#
#app = dash.Dash(__name__)
#mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'
#app.scripts.append_script({ 'external_url' : mathjax })
#
#app.layout = html.Div(id='main',children=[
#  html.P(children='Delicious \(\pi\) is inline with my goals.'),
#  html.P(children='$$ \lim_{t \\rightarrow \infty} \pi = 0$$'),
#  html.P(style={'text-align':'left'}, children='\(\\leftarrow \pi\)'),
#  html.P(style={'text-align':'left'}, children='not much left.'),
#  html.P(style={'text-align':'right'},children='\(\pi \\rightarrow\)'),
#  html.P(style={'text-align':'right'},children='but it feels so right.'),
#])
#
#if __name__ == '__main__':
#    app.run_server(debug=True)


import dash
import dash_html_components as html
from base64 import urlsafe_b64encode

def write_to_data_uri(s):
    """
    Writes to a uri.
    Use this function to embed javascript into the dash app.
    Adapted from the suggestion by user 'mccalluc' found here:
    https://community.plot.ly/t/problem-of-linking-local-javascript-file/6955/2
    """
    uri = (
        ('data:;base64,').encode('utf8') +
        urlsafe_b64encode(s.encode('utf8'))
    ).decode("utf-8", "strict")
    return uri

app = dash.Dash(__name__)
katex = src="https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.js"
app.scripts.append_script({ 'external_url' : katex })
auto_render = "https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/contrib/auto-render.min.js"
app.scripts.append_script({ 'external_url' : auto_render })
app.scripts.append_script({"""renderMathInElement(document.body);"""})


app.layout = html.Div(id='main',children=[

  html.P(children='Delicious \(\pi\) is inline with my goals.'),
  html.P(children='$$ \lim_{t \\rightarrow \infty} \pi = 0$$'),
  html.P(style={'text-align':'left'}, children='\(\\leftarrow \pi\)'),
  html.P(style={'text-align':'left'}, children='not much left.'),
  html.P(style={'text-align':'right'},children='\(\pi \\rightarrow\)'),
  html.P(style={'text-align':'right'},children='but it feels so right.'),
  html.Script(children='renderMathInElement(document.body);'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
