
from engine.engine import Engine

class WilloughbyEngine(Engine):
    @staticmethod
    def max_mileage_until_service() -> int:
        return 60000

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.max_mileage_until_service()
