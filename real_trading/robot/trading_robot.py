class TradingRobot:
    """Торговый робот."""

    def __init__(
            self,
            allowed_tickers=('BABA',),
    ):
        self.allowed_tickers = allowed_tickers
