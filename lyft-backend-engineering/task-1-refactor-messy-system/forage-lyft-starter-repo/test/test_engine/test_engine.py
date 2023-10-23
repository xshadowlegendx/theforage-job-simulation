
import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_capulet_engine_should_not_be_service_if_not_reach_max_mileage_for_service(self):
        current_mileage = 20
        last_service_mileage = 1024

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_capulet_engine_should_be_service_if_reach_max_mileage_for_service(self):
        current_mileage = CapuletEngine.max_mileage_until_service()
        last_service_mileage = -2

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_service_if_warning_light_not_on(self):
        engine = SternmanEngine(False)

        self.assertFalse(engine.needs_service())

    def test_sternman_engine_should_be_service_if_warning_light_on(self):
        engine = SternmanEngine(True)

        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_service_if_not_reach_max_mileage_for_service(self):
        current_mileage = 20
        last_service_mileage = 1024

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_service_if_reach_max_mileage_for_service(self):
        current_mileage = WilloughbyEngine.max_mileage_until_service()
        last_service_mileage = -2

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
