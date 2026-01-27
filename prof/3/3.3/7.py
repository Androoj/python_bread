"""
Функция is_available_date() 🌶️

Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования.
Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']


date_for_booking — одиночная строковая дата или период (две даты через дефис),
на который гость желает забронировать номер, например:
'01.11.2021' или '01.11.2021-04.11.2021'


Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступен для бронирования.
В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.
"""

from datetime import date, datetime


def convert_row_to_date(row: str) -> date:
    return datetime.strptime(row, '%d.%m.%Y').date()


def convert_books_to_dates(dates: list[str] | str) -> list[date]:

    result = []
    items = [dates] if isinstance(dates, str) else dates

    for item in items:
        if '-' in item:
            start_period, end_period = item.split('-')
            start_period = convert_row_to_date(start_period)
            end_period = convert_row_to_date(end_period)
            for ordinal_day in range(
                start_period.toordinal(), end_period.toordinal() + 1
            ):
                result.append(date.fromordinal(ordinal_day))

        else:
            result.append(convert_row_to_date(item))

    return result


def is_available_date(booked_dates: list[str], date_for_booking: str) -> bool:

    booked_dates_obj = convert_books_to_dates(booked_dates)
    requested_dates_obj = convert_books_to_dates(date_for_booking)

    for date_ in requested_dates_obj:
        if date_ in booked_dates_obj:
            return False
    return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
