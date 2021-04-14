import pandas as pd

from modeling.predictor.regression_based import RegressionBasedPredictor
from strategies.base import BaseStrategy


class RegressionBasedStrategy(BaseStrategy):
    """Стратегия, которая базируется на регрессии."""

    def __init__(
            self,
            estimator: RegressionBasedPredictor,
            buy_tres: float = 0.001,
            sell_tres: float = -0.001,
    ):
        super().__init__()
        self.estimator: RegressionBasedPredictor = estimator

        self.buy_tres = buy_tres
        self.sell_tres = sell_tres

    def update(self, raw: pd.Series) -> None:
        """Обновляем информацию, известную стратегии."""
        self.known_df = self.known_df.append(raw)[-self.estimator.n_prices:]

    def get_action(self):
        """Получаем решение."""
        if len(self.known_df) < self.estimator.n_prices:
            print('forced_skip')
            return "skip"

        pred = self.estimator.predict(self.known_df)[0]

        today = self.known_df[['close']].values[-1]

        diff = (pred - today) / today


        print(diff, pred, today)
        if diff >= self.buy_tres:
            return 'buy'

        if diff <= self.sell_tres:
            return 'sell'

        return 'skip'
