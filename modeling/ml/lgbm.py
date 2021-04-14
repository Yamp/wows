from lightgbm import LGBMRegressor


class LGBMStockPredictor:
    """Предсказание цен акций на основе LightGBM."""
    def __init__(
            self,
            n_prices: int = 10,
            max_horizon: int = 5,
    ):
        self.reg = LGBMRegressor()

    # def fit
