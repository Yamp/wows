from typing import Union, Callable

import pandas as pd


class StockPredictionScoring:
    """Скорим акции предсказание акций."""

    def __init__(
            self,
            metric: Union[str, Callable],
            folds: int,
    ):
        self.metric = metric

    # def score(self, df: pd.DataFrame):

    def score(self, df: pd.DataFrame):
        pass
