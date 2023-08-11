from car import Car

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire


class CarFactory:

    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(wear_sensors)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(wear_sensors)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on, wear_sensors):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(wear_sensors)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(wear_sensors)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(wear_sensors)
        car = Car(engine, battery, tire)
        return car
