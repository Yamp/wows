from typing import Callable, Optional

import numpy as np
import pandas as pd
import sklearn.base
import xgboost

from xgboost.sklearn import XGBRegressor
from fastcore.basics import ifnone
from loguru import logger
from sklearn.neighbors import KNeighborsRegressor

from strategies.ml.feature_extractor import DataFeatureExtractor
from strategies.ml.feaure_preprocessors import FeatureNormalizer


class RegressionBasedPredictor:
    """Предиктор, который основан на регрессии."""

    def __init__(
            self,
            estimator: sklearn.base.BaseEstimator,
            n_prices: int = 10,
            horizon: int = 1,
    ):
        # классы, для обработки данных
        self.reg: sklearn.base.BaseEstimator = estimator
        self.feature_extractor = DataFeatureExtractor(
            n_prices=n_prices,
            horizon=horizon,
        )
        self.normalizer = FeatureNormalizer()

        self.n_prices = n_prices
        self.horizon = horizon

    # ----------------------------------------------------------------------------------------------------------------
    # Публичный интерфейс
    # ----------------------------------------------------------------------------------------------------------------

    def fit(self, df: pd.DataFrame) -> None:
        """Обучаем регрессор."""
        logger.info('Извлекаем фичи...')
        X, y = self.feature_extractor.extract_features(df)

        logger.info(f'Нормируем фичи... {X.shape, y.shape}')
        self.normalizer.fit_transform(X, y)

        logger.info(f'Обучаемся... {X.shape, y.shape}')
        self.reg.fit(X, y.reshape(-1, 1))

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        """Получаем предикт."""
        X, _ = self.feature_extractor.extract_features(df, get_y=False)
        self.normalizer.fit_transform(X)
        self.reg.predict(X)

        pred = self.reg.predict(X)
        self.normalizer.restore(y=pred)

        return pred

    def score(
            self,
            df: pd.DataFrame,
            metric: Callable = sklearn.metrics.r2_score,
            horizon: Optional[int] = None,
    ) -> float:
        """Считаем насколько хорошо получилось."""
        horizon = ifnone(horizon, self.feature_extractor.horizon)
        min_y = self.feature_extractor.n_prices + horizon - 1

        X, y_true = self.feature_extractor.extract_features(df)
        y_pred = self.predict(df)

        return metric(y_true=y_true, y_pred=y_pred)


class KNNRegressionPredictor(RegressionBasedPredictor):
    """Предиктор, который основан на KNN."""

    def __init__(
            self,
            n_prices: int = 10,
            horizon: int = 1,

            n_neighbors: int = 5,
            weights: str = 'uniform',
            p: float = 2,
            n_jobs: int = -1,
    ):
        estimator = KNeighborsRegressor(
            n_neighbors=n_neighbors,
            weights=weights,
            p=p,
            n_jobs=n_jobs,
        )
        super().__init__(
            estimator=estimator,
            n_prices=n_prices,
            horizon=horizon,
        )


class XGBRegressionPredictor(RegressionBasedPredictor):
    """Предиктор, который основан на KNN."""

    def __init__(
            self,
            n_prices: int = 10,
            horizon: int = 1,

            n_estimators: int = 1000,
            max_depth: int = 4,
            learning_rate: Optional[float] = None,
            reg_lambda: Optional[float] = None,

            n_jobs: int = -1,
    ):
        estimator = XGBRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            reg_lambda=reg_lambda,
            n_jobs=n_jobs,
        )
        super().__init__(
            estimator=estimator,
            n_prices=n_prices,
            horizon=horizon,
        )
