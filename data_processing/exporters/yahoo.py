from datetime import datetime

import pandas as pd
from yahoo_earnings_calendar import YahooEarningsCalendar


class YahooDataExporter:
    """Скачиваем финансовые данные с yahoo."""

    def __init__(self):
        self.yec: YahooEarningsCalendar = YahooEarningsCalendar()

    def download_earnings_calendar(self) -> pd.DataFrame:
        """Скачиваем earnings calendar с yahoo.

        BMO — before the market opens
        AMC — after the market closes
        TAS/TNS — time not specified
        """
        earnings_list = self.yec.earnings_between(datetime(2001, 1, 1), datetime(2022, 1, 1))
        return pd.DataFrame(earnings_list)

    def download_earnings_for_date(
            self,
            date: datetime,
    ) -> pd.DataFrame:
        """Скачиваем заработок за 1 день."""
        earnings_list = self.yec.earnings_on(date)
        return pd.DataFrame(earnings_list)
