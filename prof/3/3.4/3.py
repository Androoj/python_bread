"""
Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

Формат входных данных
На вход программе подается дата в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.
"""

from datetime import datetime, timedelta

my_date = input()

print((datetime.strptime(my_date, '%d.%m.%Y') - timedelta(hours=24)).strftime('%d.%m.%Y'))
print((datetime.strptime(my_date, '%d.%m.%Y') + timedelta(hours=24)).strftime('%d.%m.%Y'))
