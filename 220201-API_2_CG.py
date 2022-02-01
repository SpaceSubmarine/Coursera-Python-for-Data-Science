#pip install pycoingeko
from h11 import Data
import pycoingecko
import pandas as pd
import plotly.graph_objs as go

from pycoingecko import CoinGeckoAPI
import plotly

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency = "EUR", days=30)

#print(bitcoin_data["prices"])

data = pd.DataFrame(bitcoin_data, columns=["TimeStamp", "Price"])
data["Date"] = pd.to_datetime(data["TimeStamp"], unit= "ms")
candlestick_data = data.groupby(data.Date.dt.date).agg({"Price": ["min", "max", "first", "last"]})

fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index,
                open=candlestick_data["Price"]["first"],
                high=candlestick_data["Price"]["max"],
                low=candlestick_data["Price"]["min"],
                close=candlestick_data["Price"]["last"]
                )]

#arreglar esto
fig.update_layout(xaxis_rangeslider_visible = False, xaxis_title='Date', yaxis_title='Price (EUR €)', title='Bitcoin Candlestick chart Over Past 30 Days' )

plot(fig, filename="bitcoin_candlestick_graph.html")