import pandas as pd
from prophet import Prophet


class ProphetStocksModel:
    """Предсказываем цену акций при помощи prophet."""

    def __init__(
            self,
            max_horizon: int = 10,
            # regressor: int = 10,
    ):

        # параметры
        self.max_horizon: int = max_horizon

        # вспомогательные объекты
        self.regressors = {}


    def initialize(self):
        """Инициализируем внутренние объекты."""

        self.regressors = {
            "high": {},
            "low": {},
            "close": {},
        }

        for h in range(self.max_horizon):
            for k in self.regressors:
                self.regressors[k][h] = Prophet()


    def fit(
            self,
            df: pd.DataFrame,
    ):

        ...

    def fit_prophet(self) -> None:
        """Обучаем одного prophet."""
