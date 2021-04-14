import pandas_ta
import yahoo_fin.stock_info as si

data = si.get_data("aapl")
data.ta.adjusted = "adjclose"
print(data.ta.tsi())
