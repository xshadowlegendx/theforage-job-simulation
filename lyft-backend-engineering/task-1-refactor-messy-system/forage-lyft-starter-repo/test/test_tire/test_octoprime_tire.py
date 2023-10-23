
import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_should_not_require_service_if_service_wearing_condition_not_met(self):
        tire = OctoprimeTire([0.8, 0.7, 0.8, 0.3])

        self.assertFalse(tire.needs_service())

    def test_octoprime_tire_should_require_service_if_service_wearing_condition_met(self):
        tire = OctoprimeTire([0.9, 0.9, 0.5, 0.8])

        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
