
import unittest
from datetime import datetime

from car import CarFactory
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCar(unittest.TestCase):
    def test_create_calliope_car(self):
        car = CarFactory.create_calliope(
            current_date=datetime.today().date(),
            last_service_date=datetime.today().date(),
            current_mileage=0,
            last_service_mileage=0,
            tire_wearings=[.0, .0, .0, .0])

        self.assertTrue(isinstance(car.engine, CapuletEngine))
        self.assertTrue(isinstance(car.battery, SpindlerBattery))
        self.assertFalse(car.needs_service())

    def test_create_glissade_car(self):
        car = CarFactory.create_glissade(
            current_date=datetime.today().date(),
            last_service_date=datetime.today().date(),
            current_mileage=0,
            last_service_mileage=0,
            tire_wearings=[.0, .0, .0, .0])

        self.assertTrue(isinstance(car.engine, WilloughbyEngine))
        self.assertTrue(isinstance(car.battery, SpindlerBattery))
        self.assertFalse(car.needs_service())

    def test_create_palindrome_car(self):
        car = CarFactory.create_palindrome(
            current_date=datetime.today().date(),
            last_service_date=datetime.today().date(),
            warning_light_on=False,
            tire_wearings=[.0, .0, .0, .0])

        self.assertTrue(isinstance(car.engine, SternmanEngine))
        self.assertTrue(isinstance(car.battery, SpindlerBattery))
        self.assertFalse(car.needs_service())

    def test_create_rorschach_car(self):
        car = CarFactory.create_rorschach(
            current_date=datetime.today().date(),
            last_service_date=datetime.today().date(),
            current_mileage=0,
            last_service_mileage=0,
            tire_wearings=[.0, .0, .0, .0])

        self.assertTrue(isinstance(car.engine, WilloughbyEngine))
        self.assertTrue(isinstance(car.battery, NubbinBattery))
        self.assertFalse(car.needs_service())

    def test_create_thovex_car(self):
        car = CarFactory.create_thovex(
            current_date=datetime.today().date(),
            last_service_date=datetime.today().date(),
            current_mileage=0,
            last_service_mileage=0,
            tire_wearings=[.0, .0, .0, .0])

        self.assertTrue(isinstance(car.engine, CapuletEngine))
        self.assertTrue(isinstance(car.battery, NubbinBattery))
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
