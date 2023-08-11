from tires.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, wear_sensors):
        self.__wear_sensors = wear_sensors
    
    def needs_service(self):
        return sum(self.__wear_sensors) >= 3