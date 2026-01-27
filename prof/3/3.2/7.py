"""
Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня равна его возрасту.
Год рождения Тимура — 1992, возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке,
в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.

Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего не должна выводить.
"""

from datetime import date


def print_good_dates(dates: list[date | None]) -> date | None:
    interesting_dates = []

    for date_ in dates:
        if int(date_.year) == 1992 and (int(date_.month) + int(date_.day)) == 29:
            interesting_dates.append(date_)

    interesting_dates.sort()
    interesting_dates = map(
        lambda x: x.strftime('%B %d, %Y'), interesting_dates
    )
    print(*interesting_dates, sep='\n')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]

print_good_dates(dates)
