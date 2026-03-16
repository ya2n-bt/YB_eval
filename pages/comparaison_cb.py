import dash
from dash import Input, Output
import pandas as pd
import plotly.express as px
from pathlib import Path

file_path = Path(__file__).parent.parent / "datas" / "avocado.csv"

try:
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
except FileNotFoundError:
    df = pd.DataFrame()

@dash.callback(
    Output("graph-1", "figure"),
    Output("graph-2", "figure"),
    Input("region-compare-1", "value"),
    Input("region-compare-2", "value")
)
def update_graphs(region1, region2):
    if df.empty or not region1 or not region2:
        return {}, {}

    df1 = df[df["region"] == region1].groupby("Date")["AveragePrice"].mean().reset_index()
    df2 = df[df["region"] == region2].groupby("Date")["AveragePrice"].mean().reset_index()

    y_min = min(df1["AveragePrice"].min(), df2["AveragePrice"].min()) * 0.95 
    y_max = max(df1["AveragePrice"].max(), df2["AveragePrice"].max()) * 1.05 

    fig1 = px.line(
        df1, 
        x="Date", 
        y="AveragePrice", 
        title=f"Prix moyen dans le temps - {region1}",
        labels={"AveragePrice": "Prix moyen ($)", "Date": "Date"}
    )
    fig1.update_yaxes(range=[y_min, y_max])
    fig1.update_layout(template="plotly_white")

    fig2 = px.line(
        df2, 
        x="Date", 
        y="AveragePrice", 
        title=f"Prix moyen dans le temps - {region2}",
        labels={"AveragePrice": "Prix moyen ($)", "Date": "Date"}
    )
    fig2.update_yaxes(range=[y_min, y_max])
    fig2.update_layout(template="plotly_white")

    return fig1, fig2