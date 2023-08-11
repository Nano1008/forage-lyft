from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.__engine = engine
        self.__battery = battery
        self.__tire = tire


    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tire.needs_service()
