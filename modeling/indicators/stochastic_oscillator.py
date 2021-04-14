import statistics as st
from typing import Optional

import pandas as pd

from indicators.base import BaseIndicator


class StochasticOscillator(BaseIndicator):
    """Индикатор - стохастический осциллятор."""

    def __init__(
            self,
            high_period: int = 14,
            low_period: int = 14,
            moving_period: int = 3,
            low_bound: float = 0.2,
            high_bound: float = 0.2,

            initial_history: Optional[pd.DataFrame] = None,
    ) -> None:
        self.high_period = high_period
        self.low_period = low_period
        self.moving_period = moving_period
        self.low_bound = low_bound
        self.high_bound = high_bound

        self.data: pd.DataFrame = pd.DataFrame()
        self.last_ticks: list[float] = []

        self.K_history: list[float] = []
        self.D_history: list[float] = []

    def low(self) -> float:
        """Минимальное значение."""
        return self.data.iloc[-self.low_period:, 'low'].min()

    def high(self) -> float:
        """Максимальное на промежутке."""
        return self.data.iloc[-self.high_period:, 'high'].max()

    def last(self) -> float:
        """Последняя цена"""
        return self.last_ticks[-1]

    def K(self) -> float:
        """Быстрый индикатор."""
        return (self.last() - self.low()) / (self.high() - self.low())

    def D(self) -> float:
        """Сглаженный индикатор."""
        return st.mean(self.K_history[-3:])

    def check_cross_signal(self) -> float:
        """Проверяем пересечение"""
