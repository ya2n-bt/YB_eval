import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from pathlib import Path

dash.register_page(__name__, path="/comparaison", name="Comparaison entre régions")

file_path = Path(__file__).parent.parent / "datas" / "avocado.csv"
try:
    df = pd.read_csv(file_path)
    regions = sorted(df["region"].unique())
except FileNotFoundError:
    regions = []

layout = dbc.Container([
    html.H4("Prix moyen dans le temps", className="bg-primary text-white p-2 mt-4 rounded"),

    dbc.Row([
        dbc.Col([
            dbc.Badge("Région 1:", color="info", pill=True, className="mb-2 fs-6"),
            dcc.Dropdown(
                id="region-compare-1",
                options=[{"label": r, "value": r} for r in regions],
                value="Albany" if "Albany" in regions else (regions[0] if regions else None),
                clearable=False
            )
        ], xs=12, md=6, className="mb-3"),
        
        dbc.Col([
            dbc.Badge("Région 2:", color="info", pill=True, className="mb-2 fs-6"),
            dcc.Dropdown(
                id="region-compare-2",
                options=[{"label": r, "value": r} for r in regions],
                value="Atlanta" if "Atlanta" in regions else (regions[1] if len(regions)>1 else None),
                clearable=False
            )
        ], xs=12, md=6, className="mb-3")
    ], className="mt-3"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph-1")
        ], xs=12, md=6),
        
        dbc.Col([
            dcc.Graph(id="graph-2")
        ], xs=12, md=6)
    ])
], fluid=True)