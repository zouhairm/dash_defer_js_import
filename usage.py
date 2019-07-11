import dash_defer_js_import
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    dash_defer_js_import.Import(
    	id='jsimport',
    	src='https://codepen.io/akronix/pen/pVqzLZ.js'
    ),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('jsimport', 'src')])
def display_output(src):
    return '''
    Nothing to see here as this component doesn't render anything.
    But checkout your console, it should show output of {src} being imported
    '''.format(src=src)


if __name__ == '__main__':
    app.run_server(debug=True)
