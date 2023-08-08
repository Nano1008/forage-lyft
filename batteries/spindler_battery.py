from batteries.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.__current_date = current_date
        self.__last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 2)
        return service_threshold_date < self.__current_date