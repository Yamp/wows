from typing import Optional

import pandas as pd
from ta import add_all_ta_features


class FeatureBuilder:
    """Класс, который строит фичи."""
    def __init__(self):
        self.raw_df: Optional[pd.DataFrame] = None
        self.X: pd.DataFrame = None

    def add_ta_indicators(self) -> None:
        """Добавляем все индикаторы технического анализа."""
        self.raw_df = add_all_ta_features(
            df=self.raw_df,
            open='<OPEN>',
            high='<HIGH>',
            low='<LOW>',
            close='<CLOSE>',
            volume='<VOLUME>',
        )

    # def add_diffs(self) -> None:
    #     """Добавляем все разницы."""
