from testing.open_orders import ExchangeOrder


class TradingHistory:
    """История всей симуляции."""
    def __init__(self):
        self.orders: list[ExchangeOrder] = []

    def add_order(self, o: ExchangeOrder):
        """Добавляем новый заказ в историю."""
        self.orders += [o]

    # def money(self, day: int):
    #     """Получаем цену открытия."""
    #     return self.history.at[day, "money"]
    #
    # def stocks(self, day: int):
    #     """Получаем цену открытия."""
    #     return self.history.at[day, "stocks"]
    #
    # def passive(self, day: int):
    #     """Получаем цену открытия."""
    #     return self.history.at[day, "passive"]
    #
    # def active(self, day: int):
    #     """Получаем цену открытия."""
    #     return self.history.at[day, "active"]
