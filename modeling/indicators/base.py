from models.orders import Signal


class BaseIndicator:

    def append(self) -> Signal:
        pass
