
import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_should_not_require_service_if_service_wearing_condition_not_met(self):
        tire = CarriganTire([0.8, 0.7, 0.2, 0.3])

        self.assertFalse(tire.needs_service())

    def test_carrigan_tire_should_require_service_if_service_wearing_condition_met(self):
        tire = CarriganTire([0.9, 0.7, 0.5, 0.8])

        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
