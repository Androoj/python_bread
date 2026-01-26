"""
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.
"""

from datetime import datetime, timedelta


def num_of_sundays(year: int) -> int:
    num_of_sundays = 0
    datetime_now = datetime(year=year, month=1, day=1)
    timedelta_ = timedelta(days=1)

    while datetime_now.year != year + 1:
        if datetime_now.weekday() == 6:
            num_of_sundays += 1
        datetime_now = datetime_now + timedelta_

    return num_of_sundays
