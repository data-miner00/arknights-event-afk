from datetime import datetime
from enum import Enum


class DayOfWeek(Enum):
    def __str__(self) -> str:
        return str(self.value)

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


def from_iso_weekday_int(day: int):
    match day:
        case 1:
            return DayOfWeek.MONDAY
        case 2:
            return DayOfWeek.TUESDAY
        case 3:
            return DayOfWeek.WEDNESDAY
        case 4:
            return DayOfWeek.THURSDAY
        case 5:
            return DayOfWeek.FRIDAY
        case 6:
            return DayOfWeek.SATURDAY
        case _:
            return DayOfWeek.SUNDAY


def get_today_day_of_week():
    today = datetime.now().isoweekday()
    return from_iso_weekday_int(today)
