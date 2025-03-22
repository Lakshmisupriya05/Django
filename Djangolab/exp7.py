import dash
from dash import html, dcc
my_app = dash.Dash(__name__)
my_app.layout = html.Div([
    html.H1("Hello! This is my initial Dash Application"),
    dcc.Input(placeholder='Type your full name here...')
])
if __name__ == '__main__':
    print("Starting the Dash application...")
    my_app.run_server(debug=True)
