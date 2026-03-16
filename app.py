import dash
from dash import Dash
import dash_bootstrap_components as dbc
from pathlib import Path

pages_folder = Path(__file__).parent / "pages"

app = Dash(
    __name__,
    use_pages=True, 
    pages_folder=str(pages_folder),
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.layout = dbc.Container([
    dash.page_container 
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)