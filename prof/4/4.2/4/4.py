"""
Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях.
В первом столбце записано название компании, а во втором — зарплата очередного сотрудника.

Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты сотрудников и выводит их названия, каждое на отдельной строке.
Если две компании имеют одинаковые средние зарплаты, они должны быть расположены в лексикографическом порядке их названий.
"""

import csv

with open('salary_data.csv', encoding='utf-8') as file:

    salaries_company = {}

    rows = csv.DictReader(file, delimiter=';')
    for index, row in enumerate(rows):
        if salaries_company.get(row['company_name']):
            salaries_company[row['company_name']].append(int(row['salary']))
        else:
            salaries_company[row['company_name']] = [int(row['salary'])]

    for key, value in salaries_company.items():
        salaries_company[key] = (
            sum(salaries_company[key]) / len(salaries_company[key])
        )

    salaries_company = sorted(
        salaries_company,
        key=lambda value: (salaries_company[value], value)
    )

print(*salaries_company, sep='\n')
