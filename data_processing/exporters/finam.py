import datetime
from pathlib import Path

import pandas as pd
from bidict import bidict
from finam import Exporter, Market, LookupComparator, Timeframe
from loguru import logger


class FinamDataDownloader:
    """Класс, который скачивает финансовые данные с Finam."""

    market_to_str = bidict({
        Market.COMMODITIES: "commodities",
        Market.BONDS: "bonds",
        Market.CURRENCIES_WORLD: "currencies_world",
        Market.CURRENCIES: "currencies",
        Market.ETF: "etf",
        Market.ETF_MOEX: "etf_moex",
        Market.FUTURES: "futures",
        Market.FUTURES_ARCHIVE: "futures_archive",
        Market.FUTURES_USA: "futures_usa",
        Market.INDEXES: "indexes",
        Market.SHARES: "shares",
        Market.USA: "usa",
        Market.SPB: "spb",
    })

    tf_to_str = bidict({
        Timeframe.TICKS: "ticks",
        Timeframe.MINUTES1: "minutes1",
        Timeframe.MINUTES5: "minutes5",
        Timeframe.MINUTES10: "minutes10",
        Timeframe.MINUTES15: "minutes15",
        Timeframe.MINUTES30: "minutes30",
        Timeframe.HOURLY: "hourly",
        Timeframe.DAILY: "daily",
        Timeframe.WEEKLY: "weekly",
        Timeframe.MONTHLY: "monthly",
    })

    def __init__(
            self,
            data_dir=Path(__file__).parent.parent.parent / 'data',
            start_date=datetime.date(2001, 1, 1),
            overwrite: bool = False,
    ):
        # параметры
        self.start_date = start_date
        self.data_dir: Path = data_dir
        self.overwrite: bool = overwrite

        # объекты рани
        self.exporter = Exporter()

    def download_all(
            self,
            market: str,
            timeframe: str,
    ):
        """Скачиваем все акции США."""

        market = self.market_to_str.inverse[market]
        timeframe = self.tf_to_str.inverse[timeframe]

        df = self.find_all(market=market)

        for i, row in df.iterrows():
            logger.info(f'Скачиваем {row["code"]} {i}/{len(df)} == {int(i)/len(df)}')
            self.download_asset(id=row['id'], ticker=row['code'], timeframe=timeframe, market=market)

    def find_all(self, market: int) -> pd.DataFrame:
        """Находим все интересные нам бумаги."""
        return self.exporter.lookup(
            name='',
            market=market,
            name_comparator=LookupComparator.STARTSWITH,
        ).sort_values('code').reset_index()

    def download_asset(
            self,
            id: int,
            ticker: int,
            market: int,
            timeframe: int,
    ) -> None:
        """Скачиваем один конкретный ассет."""
        logger.info(f'Скачиваем данные в папку {self.data_dir.resolve().absolute()}')

        try:
            fname = self.get_filename(ticker=ticker, market=market, timeframe=timeframe)
            logger.info(f'Проверяем {fname.resolve().absolute()}')

            if self.overwrite or not fname.exists():
                df = self.exporter.download(
                    id_=id,
                    start_date=self.start_date,
                    end_date=None,
                    market=market,
                    timeframe=timeframe,
                    delay=1,
                    max_in_progress_retries=10,
                )
                self.save_asset(df, market=market, timeframe=timeframe, ticker=ticker)
            else:
                logger.info(f'{ticker} Пропускаем, так как уже скачан.')

        except Exception as e:  # noqa
            logger.info(f'{ticker} Ошибка скачивания. {e}')
            # raise e

    def save_asset(
            self,
            df: pd.DataFrame,
            market: int,
            timeframe: int,
            ticker: int,
    ):
        """Сохраняем результат в файл."""
        try:
            path = self.get_filename(ticker=ticker, market=market, timeframe=timeframe)
            df.to_parquet(path, compression='brotli')
        except Exception as e:  # noqa
            logger.info(f'{ticker} Ошибка сохранения. {e}')
            # raise e

    def get_filename(
            self,
            ticker: int,
            market: int,
            timeframe: int,
    ) -> Path:
        """Получаем имя файла, в которое будем все записывать."""
        m = self.get_verbose_market(market)
        t = self.get_verbose_timeframe(timeframe)

        dir_path = self.data_dir / m / t
        dir_path.mkdir(parents=True, exist_ok=True)

        return dir_path / f"{ticker}.parquet"

    def get_verbose_market(self, market: int) -> str:
        """Получаем название рынка."""
        return self.market_to_str[market]

    def get_verbose_timeframe(self, tf: int) -> str:
        """Получаем название рынка."""
        return self.tf_to_str[tf]

def main():
    s

if __name__ == "__main__":
    main()
