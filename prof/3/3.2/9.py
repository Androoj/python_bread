"""
Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

Формат входных данных
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. Концом последовательности является слово end.

Формат выходных данных
Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в зависимости от того,
является ли дата корректной, а затем вывести количество корректных дат.
"""

from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


correct_date = 0

while True:
    row = input()
    if row == 'end':
        break

    day_, month_, year_ = row.split('.')
    if is_correct(year=int(year_), month=int(month_), day=int(day_)):
        print('Корректная')
        correct_date += 1
    else:
        print('Некорректная')

print(correct_date)
