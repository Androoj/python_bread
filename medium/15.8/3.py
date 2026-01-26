"""
Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, 
если переданный аргумент является неотрицательным числом (целым или вещественным), или False в противном случае.
"""

is_non_negative_num = lambda int_row: True if int_row.upper() == int_row.lower() and '-' not in int_row and int_row.count('.') < 2 else False

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
