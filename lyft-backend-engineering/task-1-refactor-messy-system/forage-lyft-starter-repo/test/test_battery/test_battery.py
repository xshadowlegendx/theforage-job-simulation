
import unittest
from datetime import datetime, timedelta

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def test_nubbin_battery_should_not_be_service_if_not_reach_service_date(self):
        current_date = datetime.today().date()
        last_service_date = current_date + timedelta(days=-2)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_should_be_service_if_reach_service_date(self):
        current_date = datetime.today().date()
        last_service_date = current_date + timedelta(days=-NubbinBattery.service_period_as_year() * 365)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_service_if_not_reach_service_date(self):
        current_date = datetime.today().date()
        last_service_date = current_date + timedelta(days=-2)

        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_spindler_battery_should_be_service_if_reach_service_date(self):
        current_date = datetime.today().date()
        last_service_date = current_date + timedelta(days=-SpindlerBattery.service_period_as_year() * 365)

        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
