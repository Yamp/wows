from typing import Optional

import numpy as np
import pandas as pd
from loguru import logger


class FeatureNormalizer:
    """Нормализатор фичей."""
    def __init__(self):
        self.diff: Optional[float] = None
        self.mul: Optional[float] = None
        self.cols = None

    def fit(
            self,
            X: pd.DataFrame,
            y: Optional[np.ndarray] = None,
    ) -> None:
        """Вычисляем параметры."""

        # logger.info('Вычисляем средние.')
        self.cols = [c for c in X.columns if c.startswith("prev_")]
        self.diff = X.loc[:, self.cols].mean(axis=1)
        self.mul = self.diff

    def transform(
            self,
            X: pd.DataFrame,
            y: Optional[np.ndarray],
    ) -> None:
        """Преобразуем данные"""
        for c in self.cols:
            X[c] -= self.diff
            X[c] /= self.mul


        if y is not None:
            y -= self.mul.values
            y /= self.diff.values

    def restore(
            self,
            X: Optional[np.ndarray] = None,
            y: Optional[np.ndarray] = None,
    ) -> None:
        """Восстанавливаем старые значения."""
        if X is not None:
            for c in self.cols:
                X[c] *= self.mul
                X[c] += self.diff

        if y is not None:
            y *= self.mul.values
            y += self.mul.values

    def fit_transform(
            self,
            X: np.ndarray,
            y: Optional[np.ndarray] = None,
    ) -> None:
        """Сразу обучаем и преобразуем."""
        self.fit(X, y)
        self.transform(X, y)

    # ----------------------------------------------------------------------------------------------------------------
    # Разные методы, которыми данные можно нормировать
    # ----------------------------------------------------------------------------------------------------------------

    def scale_std(
            self,
            raw: np.ndarray,
    ) -> np.ndarray:
        """Приводим стандартное отклонение к 1."""
        return raw / raw.std()

    def scale_mean(
            self,
            raw: np.ndarray,
    ) -> np.ndarray:
        """Приводим среднее к 1."""
        return raw / raw.mean()

    def scale_elem(
            self,
            raw: np.ndarray,
            i: int = -1,
    ) -> np.ndarray:
        """Приводим конкретный элемент к 1."""
        return raw / raw[i]

    def normalize_minmax(
            self,
            raw: np.ndarray,
    ) -> np.ndarray:
        """Нормализуем одну строку."""
        res = raw.copy()
        res -= res.min()
        res /= res.max()
        return res

    def standardize(self, raw: np.ndarray) -> np.ndarray:
        """Приводим к стандартному виду."""
        res = raw.copy()
        res -= res.mean()
        res /= res.std()
        return res

    def standardize_on_mean(self, raw: np.ndarray) -> np.ndarray:
        """Стандартизуем, но делим на среднее."""
        res = raw.copy()
        res -= raw.mean()
        res /= raw.mean()

        return res

    def normalize_diff(self, raw: np.ndarray) -> np.ndarray:
        """Нормализуем разницу."""
        res = np.diff(raw)
        res /= raw.mean()
        return res
