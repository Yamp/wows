import datetime

import pandas as pd
from finam import Exporter, Market, LookupComparator, Timeframe
from loguru import logger


def get_all_usa() -> pd.DataFrame:
    """Получаем все, что есть на рынке USA."""
    exporter = Exporter()

    all_usa_df = exporter.lookup(
        market=Market.USA,
        name='',
        name_comparator=LookupComparator.STARTSWITH
    )
    all_usa_df.to_parquet('all_usa_meta.parquet')
    return all_usa_df


def download_usa(
        id: int,
        code: str,
) -> None:
    """Скачиваем что-то с рынка USA."""
    exporter = Exporter()
    logger.info(f'Скачиваем {code} {id}')

    try:
        data = exporter.download(
            id,
            market=Market.USA,
            start_date=datetime.date(2001, 1, 1),
            end_date=None,
            timeframe=Timeframe.MINUTES1,
            delay=3,
            max_in_progress_retries=10,
        )
    except Exception as e:
        logger.info(f'{code} Ошибка скачивания.')
        return

    try:
        data.to_parquet(f'{code}_1MIN.parquet', compression='brotli')
    except Exception as e:
        logger.info(f'{code} Ошибка сохранения.')
        return


def download_all_usa():
    """Скачиваем все данные по USA."""
    meta = get_all_usa()

    my_stocks = (
        "AAPL,TCS,SBER,AFLT,MSFT,BABA,TSLA,GOOG,PIKK,AFKS,FB,FSLY,AFKS,AMD,ATVI,BTI,ET,FIXP,HHR,JPM,"
        "MDMG,GM,OZON,VIPS,YNDX,EBAY,ALRS,FIVE,GAZP,TCSG,MVID,RUAL,TATN,SNGSP,CHMF,WMT,WFC,TDOC,LRN,"
        "FXCN,FXKZ,SNGSP,SIBN,AGRO,MAGN,NEE,TMOS,FXWO,FXUS,FXDE,VTBE"
    )

    meta = meta[meta['code'].isin(my_stocks.split(','))]

    for i, r in meta.reset_index().iterrows():
        download_usa(id=r['id'], code=r['code'])
