import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import dash_plot, modes_dsply, results


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dash_plot':
        return dash_plot.layout
    elif pathname == '/apps/modes_dsply':
        return modes_dsply.layout
    elif pathname == '/apps/results':
        return results.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)