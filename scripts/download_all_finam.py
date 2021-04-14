#!/usr/bin/env python
import logging
import sys

import fire

sys.path += ['..']

from data_processing.exporters.finam import FinamDataDownloader


def enable_logging():
    """Включаем логгирование запросов."""
    logging.basicConfig(level=logging.INFO)


def download(
        market: str = 'usa',
        timeframe: str = 'minutes1',
        log_requests: bool = True,
):
    """Скачиваем все акции."""
    if log_requests:
        enable_logging()

    downloader = FinamDataDownloader()
    downloader.download_all(market=market, timeframe=timeframe)


if __name__ == "__main__":
    fire.Fire(download)
