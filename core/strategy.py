import abc

import pandas as pd

from core.historical_data import MarketState
from core.models import ExchangeOrder


class BaseStrategy(abc.ABC):
    """Стратегия, которая базируется на регрессии."""

    def __init__(self):
        self.known_df = pd.DataFrame()

    def update(self, state: MarketState):
        """Обновляем информацию, известную стратегии."""
        self.known_df = self.known_df.append(state.row)[:50]

    @abc.abstractmethod
    def get_orders(self) -> list[ExchangeOrder]:
        """Получаем решение."""
        raise NotImplementedError()
