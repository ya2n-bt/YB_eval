import dash
from dash import dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from pathlib import Path

dash.register_page(__name__, path="/", name="Affichage des données")

file_path = Path(__file__).parent.parent / "datas" / "avocado.csv"

try:
    df = pd.read_csv(file_path)
    regions = df["region"].unique()
    types = df["type"].unique()
    
    cols_to_drop = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
    df_table = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
except FileNotFoundError:
    df_table = pd.DataFrame()
    regions = []
    types = []

type_options = [{"label": "Tous", "value": "Tous"}] + [{"label": t, "value": t} for t in types]

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label("Sélectionner une région :"),
            dcc.Dropdown(
                id="region-dropdown",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0] if len(regions) > 0 else None,
                clearable=False
            )
        ], xs=12, md=6, className="mb-3"), 
        
        dbc.Col([
            dbc.Label("Sélectionner un type :"),
            dcc.Dropdown(
                id="type-dropdown",
                options=type_options,
                value="Tous",
                clearable=False
            )
        ], xs=12, md=6, className="mb-3")
    ], className="mt-4"),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id="avocado-table",
                columns=[{"name": i, "id": i} for i in df_table.columns],
                data=df_table.head(50).to_dict("records"), 
                page_size=15,
                style_table={"overflowX": "auto"},
                style_cell={
                    "textAlign": "left", 
                    "padding": "10px",
                    "fontFamily": "sans-serif"
                },
                style_header={
                    "backgroundColor": "#007bff", 
                    "color": "white",
                    "fontWeight": "bold"
                }
            )
        ])
    ])
], fluid=True)
