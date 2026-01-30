"""
Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную строку из этого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести случайную строку указанного файла.
"""

import random

file = open('lines.txt', encoding='utf-8')

row_file = list(map(lambda row: row.strip(), file))
random_row = random.randint(0, len(row_file))

print(row_file[random_row])

file.close()
