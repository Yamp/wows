from collections import Collection


class Portfolio:
    """Мой портфель"""

    @staticmethod
    def from_tickers_and_money(
            money: float,
            tickers: list[str],
    ):
        """Создаем портфель из денег и тикеров."""

    def __init__(
            self,
            amounts: dict[str, float],
    ):
        self.amounts = amounts

    def get_amount(
            self,
            tickers: str,
    ) -> float:
        """Получаем количество заданного ассета."""
        return self.amounts[tickers]

    def estimate_money(
            self,
            prices: dict[str, float],
    ) -> float:
        """ Оцениваем наш портфель в деньгах."""
        return sum(prices[t] * a for t, a in self.amounts)

    def increase(
            self,
            ticker: str,
            amount: float,
    ):
        """Увеличиваем количество ассета в портфеле."""
        self.amounts[ticker] += amount

    def decrease(
            self,
            ticker: str,
            amount: float,
    ):
        """Увеличиваем количество ассета в портфеле."""
        self.amounts[ticker] -= amount
