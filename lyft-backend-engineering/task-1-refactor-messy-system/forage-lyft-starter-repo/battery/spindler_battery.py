
from battery.battery import Battery

class SpindlerBattery(Battery):
    @staticmethod
    def service_period_as_year():
        return 3

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        # note:
        # in order to be year accurate, can use dateutil library
        # for now assuming 365 days is one year to service
        return (self.current_date - self.last_service_date).days >= self.service_period_as_year() * 365
