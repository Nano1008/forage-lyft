import unittest
from datetime import datetime, date

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2019, 8, 8)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2019, 8, 7)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2019, 8, 9)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2021, 8, 8)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2021, 8, 7)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = date(2021, 8, 9)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
