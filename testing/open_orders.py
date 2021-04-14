from copy import deepcopy
from typing import Any, Collection

from core.models import ExchangeOrder, OrderType, OrderDirection


class ActiveExchangeOrdersLocal:
    """Класс, который показывает все открытые заявки."""

    def __init__(self):
        self.orders: dict[Any, ExchangeOrder] = {}

    def clear(
            self,
            ignore_types: Collection[OrderType],
            ignored_directions: Collection[OrderDirection],
    ) -> None:
        """Удаляем все ненужные заказы."""
        self.orders = {
            id: order
            for id, order in self.orders.items()
            if (order.type in ignore_types) or (order.direction in ignored_directions)
        }

    def replace(
            self,
            orders: Collection[ExchangeOrder],
    ):
        """Обновляем состав активных заявок."""
        self.orders = {
            o.id: o
            for o in orders
        }

    def add(self, o: ExchangeOrder) -> None:
        """Добавляем заказ."""
        self.orders[o.id] = o

    def remove(self, id: Any) -> None:
        """Добавляем заказ."""
        del self.orders[id]

    def all(self) -> list[ExchangeOrder]:
        """Добавляем заказ."""
        return list(self.orders.values())
