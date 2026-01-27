"""
Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:

dates — список строковых дат в формате DD.MM.YYYY
Функция должна возвращать список, в котором содержатся все даты из списка dates,
расположенные в порядке возрастания, а также все недостающие промежуточные даты.
"""
from datetime import date, datetime, timedelta


def fill_up_missing_dates(dates: list[str]) -> list[date]:

    formatted_dates = [
        datetime.strptime(str_date, '%d.%m.%Y').date() for str_date in dates
    ]

    count_of_min_max = (max(formatted_dates) - min(formatted_dates)).days
    result = []

    for item in range(count_of_min_max + 1):
        result.append(
            (min(formatted_dates) + timedelta(days=item)).strftime('%d.%m.%Y')
        )

    return result


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
