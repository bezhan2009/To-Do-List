import random as r
from datetime import datetime

from datagen.src.errors.generator_errors import errors
from datagen.src.generators.date.dataclass import GeneratedDate


def generate_date(day: int = 0, month: int = 0, year: int = 0, hour: int = None, minute: int = None,
                  second: int = None):
    """
    Generates a random date and optional time.

    :param day: Day of the month. If 0, a random value from 1 to 28 is generated.
    :param month: Month of the year. If 0, a random value from 1 to 12 is generated.
    :param year: Year. If 0, a random value from 1970 to 2050 is generated.
    :param hour: Hour of the day. If None, it is not included in the output.
    :param minute: Minute of the hour. If None, it is not included in the output.
    :param second: Second of the minute. If None, it is not included in the output.
    :return: A GeneratedDate object with the specified or random values.
    """
    if day > 28 and month == 2:
        raise errors.DateGetError("Invalid day for February. Please provide a day between 1 and 28.")
    if day > 31:
        raise errors.DateGetError("Invalid day. Please provide a day between 1 and 31.")
    if month > 12 or month < 0:
        raise errors.DateGetError("Invalid month. Please provide a month between 1 and 12.")
    if hour is not None and (hour > 23 or hour < 0):
        raise errors.DateGetError("Invalid hour. Please provide an hour between 0 and 23.")
    if minute is not None and (minute > 59 or minute < 0):
        raise errors.DateGetError("Invalid minute. Please provide a minute between 0 and 59.")
    if second is not None and (second > 59 or second < 0):
        raise errors.DateGetError("Invalid second. Please provide a second between 0 and 59.")

    if day == 0:
        day = r.randint(1, 28)
    if month == 0:
        month = r.randint(1, 12)
    if year == 0:
        year = r.randint(1970, 2050)

    if hour is None and minute is None and second is None:
        return GeneratedDate(datetime(year, month, day))
    else:
        if hour is None:
            hour = 0
        if minute is None:
            minute = 0
        if second is None:
            second = 0
        return GeneratedDate(datetime(year, month, day, hour, minute, second))
