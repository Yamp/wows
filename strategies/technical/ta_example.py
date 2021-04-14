import yahoo_fin.stock_info as si
from ta import add_all_ta_features
from ta.momentum import RSIIndicator

# pull data from Yahoo Finance
data = si.get_data("aapl")

data = add_all_ta_features(
    data,
    open="open",
    high="high",
    low="low",
    close="adjclose",
    volume="volume",
)


rsi_21 = RSIIndicator(close=data.adjclose, window=21)
data["rsi_21"] = rsi_21.rsi()

print(list(data.columns))
print(data.momentum_rsi.tail())
