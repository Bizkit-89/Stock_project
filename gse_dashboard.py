import dash
from dash import dcc, html
import pandas as pd
import requests
from datetime import datetime

# Function to fetch live GSE stock data
def fetch_gse_stock(symbol):
    url = f"https://dev.kwayisi.org/apis/gse/live/{symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame([data])
        df['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return df
    else:
        return pd.DataFrame()

# Fetch MTNGH data
df = fetch_gse_stock("MTNGH")

# Create Dash app
app = dash.Dash(__name__)
app.title = "GSE Stock Dashboard"

app.layout = html.Div([
    html.H1("MTN Ghana Stock Tracker (MTNGH)", style={'textAlign': 'center'}),

    html.Div([
        html.P(f"Latest Price: {df['price'].values[0]} GHS"),
        html.P(f"Previous Price: {df['prev'].values[0]} GHS"),
        html.P(f"Change: {df['change'].values[0]} GHS"),
        html.P(f"Volume: {df['volume'].values[0]}")
    ], style={'textAlign': 'center', 'fontSize': 18}),

    dcc.Graph(
        id='price-trend',
        figure={
            "data": [{
                "x": [df['date'].values[0]],
                "y": [df['price'].values[0]],
                "type": "line",
                "name": "MTNGH"
            }],
            "layout": {
                "title": "Price Trend (Add historical data to expand)",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Price (GHS)"}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
