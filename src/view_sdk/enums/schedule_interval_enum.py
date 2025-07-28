from enum import Enum

class ScheduleIntervalEnum(str, Enum):
    OneTime = "OneTime"
    SecondsInterval = "SecondsInterval"
    MinutesInterval = "MinutesInterval"
    HoursInterval = "HoursInterval"
    DaysInterval = "DaysInterval" 