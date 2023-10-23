
from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wearings: list[float]):
        self.wearings = wearings
        self.__is_need_service = len([w for w in self.wearings if w >= 0.9]) > 1

    def needs_service(self) -> bool:
        return self.__is_need_service

