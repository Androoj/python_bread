"""
Напишите функцию is_num(), используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, 
если переданный аргумент является числом (целым или вещественным), или False в противном случае.
"""

is_num = lambda int_row: True if (int_row.upper() == int_row.lower() and int_row.count('.') < 2 and int_row.count('-') < 2 and '-' not in int_row[1:]) or (int_row.upper() == int_row.lower() and int_row.count('.') < 2 and int_row.count('-') < 2 and int_row.startswith('-')) else False


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))
