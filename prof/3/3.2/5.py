"""
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO-формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
"""

from datetime import datetime

INPUT_DATE_FORMAT = '%Y-%m-%d'
OUTPUT_DATE_FORMAT = '%d-%m (%Y)'

x, y = datetime.strptime(input(), INPUT_DATE_FORMAT), datetime.strptime(input(), INPUT_DATE_FORMAT)

print(
    min(x, y).strftime(OUTPUT_DATE_FORMAT)
)
