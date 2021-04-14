from typing import Collection


class TradingStrategy:
    """Описание торговой стратегии."""

    def __init__(
            self,
            allowed_stocks: Collection[str],
    ):
        pass

    def update(self, event):
