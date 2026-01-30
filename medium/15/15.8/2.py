"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, 
если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен), или False в противном случае.
"""

func = lambda row: True if row[0].lower() == 'a' and row[-1].lower() == 'a' else False

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
