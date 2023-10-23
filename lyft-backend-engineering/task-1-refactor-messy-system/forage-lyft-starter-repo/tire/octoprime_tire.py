
from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wearings: list[float]):
        self.wearings = wearings
        self.__is_need_service = sum(wearings) >= 3

    def needs_service(self) -> bool:
        return self.__is_need_service


