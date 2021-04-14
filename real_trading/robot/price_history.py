import datetime
from collections import Collection
from numbers import Number
from typing import Dict, List

import pandas as pd
from tinvest import Candle


class PriceHistory:
    """История цены для расчета всякого разного."""

    def __init__(
            self,
            timeframes: Collection[int] = (60, 300, 600, 1800, 3600),
    ):
        self.timeframes: Collection[int] = timeframes
        self.candles: Dict[int, pd.DataFrame] = {}

        self.last_ticks: List = []

    def append(
            self,
            price: Number,
            volume: Number,
            dt: datetime.datetime,
    ):
        """Добавляем новый тик."""
        self.last_ticks += price

        if int(dt.timestamp()) % 60 == 0:
            ...
