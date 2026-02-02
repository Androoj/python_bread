"""
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv-файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список элементов этого столбца.
"""

import csv


def csv_columns(filename: str) -> dict:

    with open(filename, encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',')

        result = {}

        for key in rows.fieldnames:
            result.setdefault(key, [])

        for row in rows:
            for key in rows.fieldnames:
                result[key].append(row[key])

    return result


print(csv_columns('movie.csv'))
