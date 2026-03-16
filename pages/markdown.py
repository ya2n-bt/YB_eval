import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from pathlib import Path

dash.register_page(__name__, path="/markdown", name="Présentation de Dash")

base_path = Path(__file__).parent.parent / "assets"

def read_md_file(filename):
    try:
        with open(base_path / filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"**Erreur :** Le fichier {filename} est introuvable dans le dossier assets/."

contenu_accueil = read_md_file("expli1.md")
contenu_layout = read_md_file("expli2.md")
contenu_callback = read_md_file("expli3.md")

banniere = html.Div(
    html.H2("PRÉSENTATION DE DASH", className="text-white text-center text-uppercase m-0", style={"letterSpacing": "2px"}),
    style={
        "backgroundImage": "url('/assets/dash.jpg')", 
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "padding": "40px 20px", 
        "marginBottom": "20px",
        "borderRadius": "5px"
    }
)

accordeon = dbc.Accordion(
    [
        dbc.AccordionItem(
            dcc.Markdown(contenu_accueil),
            title="Accueil"
        ),
        dbc.AccordionItem(
            dcc.Markdown(contenu_layout),
            title="Layout"
        ),
        dbc.AccordionItem(
            dcc.Markdown(contenu_callback),
            title="CallBack"
        ),
    ]
)

layout = dbc.Container([
    html.Br(),
    banniere,
    accordeon
], fluid=True, className="mt-4")