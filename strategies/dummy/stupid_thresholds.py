

# def strat():
#     if (pred - today_price) / today_price >= 0.001:
#         return 'buy'
#
#     if (pred - today_price) / today_price <= -0.001:
#         return 'sell'
#
#     return 'skip'

# n = 20
# last_n_days = [self.close(d) for d in range(max(self.cur_day - n, 0), self.cur_day + 1)]
# *others, today_price = last_n_days
# max_change = max((o - today_price) / o for o in others)
# min_change = min((o - today_price) / o for o in others)


# if min_change <= -0.05:
#     return "buy"
#
# if min_change <= -0.005:
#     return "sell"
#
# if max_change >= 0.005:
#     return "buy"
#
# if max_change >= 0.05:
#     return "sell"

# return 'skip'
