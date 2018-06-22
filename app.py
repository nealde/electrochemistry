import dash

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
#mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'
mathjax = "https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.js"
app.scripts.append_script({ 'external_url' : mathjax })

