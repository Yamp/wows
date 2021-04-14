"""Базовые классы для всего, что касается трейдинга."""
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Any

OrderType = Literal["limit", "market", "recurring_limit"]
OrderDirection = Literal["sell", "buy"]


@dataclass
class ExchangeOrder:
    """Биржевая заявка."""
    id: Any
    ticker: str
    type: OrderType
    direction: OrderDirection
    amount: float
    limit: int


@dataclass
class Candle:
    """Одна свеча."""
    date: datetime
    open: float
    close: float
    high: float
    low: float
