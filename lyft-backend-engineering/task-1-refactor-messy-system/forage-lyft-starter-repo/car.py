
from abc import ABC, abstractmethod

from tire.tire import Tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Serviceable(ABC):
    @abstractmethod
    def needs_service() -> bool:
        raise NotImplementedError

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.tire = tire
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wearings) -> Car:
        tire = CarriganTire(tire_wearings)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wearings) -> Car:
        tire = CarriganTire(tire_wearings)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wearings) -> Car:
        tire = OctoprimeTire(tire_wearings)
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wearings) -> Car:
        tire = OctoprimeTire(tire_wearings)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wearings) -> Car:
        tire = CarriganTire(tire_wearings)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery, tire)
