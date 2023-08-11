from tires.tire import Tire

class CarriganTire(Tire):

    def __init__(self, wear_sensors):
        self.__wear_sensors = wear_sensors

    def needs_service(self):
        return max(self.__wear_sensors) >= 0.9