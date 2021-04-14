from collections import Iterator
from pathlib import Path

import pandas as pd

from core.models import Candle


class MarketState:
    """Состояние рынка в конкретный момент времени."""

    def __init__(
            self,
            num: int,
            row: pd.Series,
    ):
        self.num: int = num
        self.row: pd.Series = row

    def get_candle(self) -> Candle:
        """Получаем свечку."""


class HistoricalData:
    """Класс, который представляет из себя исторические данные."""

    def __init__(
            self,
            dir: Path = Path('../data'),
    ):
        self.dir: Path = dir

        self.df: pd.DataFrame = pd.DataFrame()

    def size(self):
        """Размер данных."""
        return len(self.df)

    def tickers(self) -> list[str]:
        """Получаем все существующие тикеры."""
        raise NotImplementedError()

    def get_candle(
            self,
            ticker: str,
            num: int,
    ) -> Candle:
        """Получаем свечку."""
        return Candle()

    def states(self) -> Iterator[MarketState]:
        """Получаем итератор для состояний."""
        for i, r in self.df.iterrows():
            yield MarketState(r)
