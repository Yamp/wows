from typing import Optional

import numpy as np
import pandas as pd
from loguru import logger


class DataFeatureExtractor:
    """Извлекаем фичи из данных."""

    def __init__(
            self,
            n_prices: int,
            horizon: int = 0,
            data_col: str = 'close',
    ):
        self.n_prices: int = n_prices
        self.horizon: int = horizon

        self.data_col: str = data_col

    def extract_features(
            self,
            df: pd.DataFrame,
            get_y: bool = True,
    ) -> tuple[np.array, Optional[np.array]]:
        """Превращаем данные в фичи. """

        data_arr = df[self.data_col].values

        if get_y:
            min_y_idx = self.n_prices + self.horizon - 1
            samples_num = len(df) - self.n_prices - self.horizon + 1

            logger.debug(f'{min_y_idx}, {samples_num}, {self.horizon}, {self.n_prices}, {len(df)}')
            assert len(df) - min_y_idx >= 1
            X = np.array([
                data_arr[k: k + self.n_prices]
                for k in range(samples_num)]
            )

            y = data_arr[min_y_idx:].copy() if get_y else None

            # return X

            # X = pd.DataFrame(X, columns=[f'prev_{i}' for i in range(self.n_prices)])
            # X = pd.concat([df[self.n_prices - 1:], X], axis=1)
            # X = X[:len(y)]
            #
            # logger.info(f'{len(X)}, {y.shape}')
        else:
            X = np.array([
                data_arr[k: k + self.n_prices]
                for k in range(len(df) - self.n_prices + 1)]
            )
            # X = pd.DataFrame(X, columns=[f'prev_{i}' for i in range(self.n_prices)])
            # X = pd.concat([df[self.n_prices - 1:], X], axis=1)

            y = None

        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        return X, y

    # def extract_prices(
    #         self,
    # ):
    #     """Извлекаем данные цен."""
    #
