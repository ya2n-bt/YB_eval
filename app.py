import dash
from dash import Dash, html
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

nav_links = [
    dbc.NavItem(dbc.NavLink(page["name"], href=page["path"], active="exact"))
    for page in dash.page_registry.values()
]

navbar = dbc.NavbarSimple(
    children=nav_links,
    brand=html.B("Application des M2 MECEN"),
    brand_href="/",
    color="primary", 
    dark=True,       
    fluid=True,
    className="mb-4" 
)

app.layout = dbc.Container([
    navbar,
    dash.page_container 
], fluid=True, className="p-0") 

import pages.table_cb
import pages.comparaison_cb

if __name__ == "__main__":
    app.run(debug=True)
