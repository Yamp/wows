import btalib
import yahoo_fin.stock_info as si

# говорят, у нее классные доки
data = si.get_data("aapl")
stoch = btalib.stochastic(data)

print(stoch.df)
