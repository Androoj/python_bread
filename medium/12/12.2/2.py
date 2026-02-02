"""
Почтовый индекс в Латверии имеет вид:

LetterLetterNumber_NumberLetterLetter:
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
"""

import random
import string


def generate_index() -> str:

    letter = random.choice(string.ascii_uppercase)
    number = random.randint(0, 99)

    return f'{letter}{letter}{number}_{number}{letter}{letter}'


print(generate_index())
