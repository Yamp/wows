import random

import pandas as pd
from loguru import logger

from core.historical_data import HistoricalData
from core.models import ExchangeOrder, OrderType
from core.strategy import BaseStrategy
from testing.open_orders import ActiveExchangeOrdersLocal
from testing.portfolio import Portfolio
from testing.trading_history import TradingHistory


class TradingStrategyTester:
    """Класс, который проверяет трейдинговую стратегию."""

    def __init__(
            self,
            strategy: BaseStrategy,
            df: pd.DataFrame,
            initial_money: float = 100,
            commission: float = 0.025 / 100,
            max_short: float = 0.3,
    ) -> None:
        # Входные параметры симулятора
        self.strategy: BaseStrategy = strategy
        self.commission: float = commission
        self.max_short: float = max_short

        # Вспомогательные объекты
        self.data: HistoricalData = HistoricalData(df)
        self.open_orders: ActiveExchangeOrdersLocal = ActiveExchangeOrdersLocal()  # активные заявки
        self.history: TradingHistory = TradingHistory()
        self.portfolio: Portfolio = Portfolio.from_tickers_and_money(initial_money, tickers=self.data.tickers())

        # Вспомогательные объекты
        self.candle_num: int = 0  # номер текущей свечки

    # ----------------------------------------------------------------------------------------------------------------
    # Обработка заказов
    # ----------------------------------------------------------------------------------------------------------------

    # TODO: конверсии долларов в рубли и тд.

    def buy(
            self,
            ticker: str,
            amount: float,
            price: float,
    ) -> None:
        """Покупаем ассет."""
        self.portfolio.increase(ticker, amount)
        self.portfolio.decrease("money", amount * price)

    def sell(
            self,
            ticker: str,
            amount: float,
            price: float,
    ) -> None:
        """Продаем ассет."""
        self.portfolio.decrease(ticker, amount)
        self.portfolio.increase("money", amount * price)

    def process_limit_order(self, o: ExchangeOrder) -> None:
        """Обрабатываем заказ."""
        candle = self.data.get_candle(o.ticker, self.candle_num)

        if o.direction == 'sell':  # лимитная продажа
            if candle.high >= o.limit:
                self.sell(o.ticker, o.amount, max(o.limit, candle.low))
        elif o.direction == 'buy':
            if candle.low <= o.limit:
                self.sell(o.ticker, o.amount, min(o.limit, candle.high))
        else:
            raise ValueError(f"Неправильная заявка {o}")

    def process_market_order(self, o: ExchangeOrder) -> None:
        """Обрабатываем рыночные заявки по текущей цене."""
        candle = self.data.get_candle(o.ticker, self.candle_num)

        if o.direction == 'sell':
            self.sell(o.ticker, o.amount, candle.close)
        else:
            self.buy(o.ticker, o.amount, candle.close)

    def process_orders(self, type: OrderType) -> None:
        """Обрабатываем заказы."""
        orders = self.open_orders.all()
        random.shuffle(orders)

        for o in orders:
            if type == o.type == 'market':
                self.process_market_order(o)
            elif type == o.type == 'limit':
                self.process_limit_order(o)

    # ----------------------------------------------------------------------------------------------------------------
    # Описание торговой стратегии
    # ----------------------------------------------------------------------------------------------------------------

    def simulate(self) -> None:
        """Запускаем симуляцию."""
        for state in self.data.states():
            self.candle_num = state.num
            self.process_orders(type='limit')
            self.strategy.update(state)
            self.open_orders.replace(self.strategy.get_orders())
            self.process_orders(type='market')
            self.log_progress()

    def log_progress(self) -> None:
        """Логгируем, что происходит."""
        logger.debug(self.candle_num)

        # last_action = self.history.at[self.cur_day, 'action']
        # if last_action != 'skip':
        #
        #     m = self.money(self.cur_day)
        #     s = self.stocks(self.cur_day)
        #     c = self.close(self.cur_day)
        #     self.history.at[self.cur_day, 'active'] = m + s * c
        #
        #     passive = self.passive(self.cur_day)
        #     active = self.active(self.cur_day)
        #
        #     color = {'buy': "green", 'sell': 'red', 'skip': 'yellow'}[last_action]
        #     rich.print(f'[{color}]{last_action} ', end=' ')
        #     rich.print(f'[bold]{passive}/{active} {self.cur_day}/{self.size}')
        #
        #     # print(
        #     #     f"money  :{self.money(self.cur_day):10.1f}, "
        #     #     f"stocks :{self.stocks(self.cur_day):10.1f}, "
        #     #     f"price  :{self.close(self.cur_day):10.1f} "
        #     #     f"passive/active:{passive:10.1f}/{active:10.1f} {passive > active} "
        #     #     f'day: {self.cur_day} {self.cur_day / self.size}'
        #     # )
