"""
Напишите программу, которая с помощью модуля random генерирует случайный пароль.
Программа принимает на вход длину пароля и выводит случайный пароль,
содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
"""

import random

length = int(input())

for _ in range(length):
    choises = {
        0: chr(random.randint(65, 90)),
        1: chr(random.randint(97, 122))
    }

    print(choises[random.randint(0, 1)], end='')
