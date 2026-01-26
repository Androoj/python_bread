"""
Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.

Формат входных данных
На вход программе подается натуральное число n, а затем n корректных дат в ISO-формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY.
"""

from datetime import datetime

DATE_FORMAT_INPUT = '%Y-%m-%d'
DATE_FORMAT_OUTPUT = '%d/%m/%Y'

result = sorted([
   datetime.strptime(input(), DATE_FORMAT_INPUT) for _ in range(int(input()))
])

for _ in result:
    print(_.strftime(DATE_FORMAT_OUTPUT))
