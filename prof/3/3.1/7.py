"""
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
"""

from datetime import date


def saturdays_between_two_dates(start: date, end: date) -> int:
    count_of_saturdays = 0

    if start < end:
        for date_ in range(start.toordinal(), end.toordinal() + 1):
            if date.fromordinal(date_).weekday() == 5:
                count_of_saturdays += 1
    for date_ in range(end.toordinal(), start.toordinal() + 1):
        if date.fromordinal(date_).weekday() == 5:
            count_of_saturdays += 1
    return count_of_saturdays


date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
