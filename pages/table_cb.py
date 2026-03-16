import dash
from dash import Input, Output
import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent.parent / "datas" / "avocado.csv"

try:
    df = pd.read_csv(file_path)
    cols_to_drop = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
    df_table = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
except FileNotFoundError:
    df_table = pd.DataFrame()

@dash.callback(
    Output("avocado-table", "data"),
    Input("region-dropdown", "value"),
    Input("type-dropdown", "value")
)
def update_table(selected_region, selected_type):
    if df_table.empty:
        return []

    filtered_df = df_table.copy()
    
    if selected_region:
        filtered_df = filtered_df[filtered_df["region"] == selected_region]
        
    if selected_type and selected_type != "Tous":
        filtered_df = filtered_df[filtered_df["type"] == selected_type]

    return filtered_df.to_dict("records")