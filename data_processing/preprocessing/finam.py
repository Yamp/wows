import datetime

import numpy as np
import pandas as pd


class FinamDataPreprocessor:
    """Класс, который препроцессит данные finam."""

    def __init__(self):
        # self.
        pass

    def preprocess(
            self,
            df: pd.DataFrame,
    ) -> pd.DataFrame:
        """Препроцессим колонки."""
        df = self.change_cols(df)
        df = self.fix_missing(df)

        return df

    def change_cols(
            self,
            df: pd.DataFrame,
    ) -> pd.DataFrame:
        """Препроцессим данные в формате финам."""

        df = df.reset_index().drop(columns='index')

        df = df.rename(columns={
            "<OPEN>": "open",
            "<CLOSE>": "close",
            "<HIGH>": "high",
            "<LOW>": "low",
            "<VOL>": "volume",
        })

        def extract_dt(raw: pd.Series):
            """Извлекаем дату и время."""
            d = raw["<DATE>"]
            t = raw["<TIME>"]

            year = int(str(d)[:4])
            month = int(str(d)[4:6])
            day = int(str(d)[6:])
            hour, minute, second = map(int, t.split(':'))

            return datetime.datetime(
                year=year, month=month, day=day,
                hour=hour, minute=minute, second=second,
            )

        df['date'] = df.apply(extract_dt, axis=1)
        df = df.drop(columns=["<DATE>", "<TIME>"])

        return df

    def fix_missing(self, df) -> pd.DataFrame:
        """Заполняем пропуски в данных."""
        cols = ["open", "close", "high", "low", "volume"]

        for c in cols:
            df.loc[df[c] <= 0, c] = np.nan
            df[c] = df[c].fillna('ffill')

        return df
