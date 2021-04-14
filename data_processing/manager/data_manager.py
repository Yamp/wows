from pathlib import Path
from typing import Literal

import pandas as pd


class DataManager:
    """Класс, который умеет получать доступ ко всем известным нам данным."""

    def __init__(
            self,
            base_dir: Path,
    ):
        self.base_dir: Path = base_dir

    # ----------------------------------------------------------------------------------------------------------------
    # Получаем данные по ценам акций
    # ----------------------------------------------------------------------------------------------------------------

    def get_asset_prices(
            self,
            ticker: str,
            tf: Literal[''],
    ) -> pd.DataFrame:
        """Получаем цены нужных нам асетов."""




    # ----------------------------------------------------------------------------------------------------------------
    # Получаем рекомендации и иже с ними
    # ----------------------------------------------------------------------------------------------------------------

    def get_forecasts(self) -> pd.DataFrame:
        """Получаем все прогнозы аналитиков."""
        tinkoff_path = 'forecasts/tinkoff_rec.parquet'
        return self.read_parquet(tinkoff_path)

    def get_ideas(self) -> pd.DataFrame:
        """Получаем все инвест-идеи."""
        tinkoff_path = 'forecasts/tinkoff_ideas.parquet'
        return self.read_parquet(tinkoff_path)

    # ----------------------------------------------------------------------------------------------------------------
    # Получение путей
    # ----------------------------------------------------------------------------------------------------------------

    def get_stock_path(self) -> Path:
        """Получаем путь к файлу с курсом конкретной акции."""


    # ----------------------------------------------------------------------------------------------------------------
    # Низкоуровневые методы.
    # ----------------------------------------------------------------------------------------------------------------

    def read_parquet(
            self,
            rel_path: str,

    ) -> pd.DataFrame:
        """Считываем данные в формате паркета."""
        path = self.get_file_path(rel_path, for_writing=False)

        return pd.read_parquet(path)

    def save_parquet(
            self,
            df: pd.DataFrame,
            rel_path: str,
            overwrite: bool = False,
    ) -> None:
        """Считываем данные в формате паркета."""
        path = self.get_file_path(rel_path, for_writing=True, overwrite=overwrite)

        df.to_parquet(
            path=path,
            compression='zstd',
            index=None,
            partition_cols=None,
        )

    def get_file_path(
            self,
            rel_path: str,
            for_writing: bool = False,
            overwrite: bool = True,
    ) -> Path:
        """Получаем путь к нужному файлу."""
        path = self.base_dir / rel_path
        file_dir = path.parents[0]
        file_dir.mkdir(parents=True, exist_ok=True)

        if not for_writing:
            if not path.is_file():
                raise ValueError(f"Несуществующий файл.")
        else:
            if path.is_file() and not overwrite:
                raise ValueError(f"Вы пытаетесь перезаписать существующий файл. {path.resolve().absolute()}")

        return path
