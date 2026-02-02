"""
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты

Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
в первом столбце записано название почтового домена,
а во втором — количество пользователей, использующих данный домен.

Домены в файле должны быть расположены в порядке возрастания количества их использований,
при совпадении количества использований — в лексикографическом порядке.
"""

import csv

with open('data.csv', encoding='utf-8') as file_input, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_output:

    csv_reader = csv.DictReader(file_input, delimiter=',')
    result = {}

    for row in csv_reader:
        domain = row['email'].split('@')[1]
        result[domain] = result.get(domain, 0) + 1

    # Сортировка по количеству (от меньшего к большему)
    sorted_dict = dict(sorted(result.items(), key=lambda item: (item[1], item[0])))

    csv_writer = csv.DictWriter(file_output, fieldnames=['domain', 'count'])
    csv_writer.writeheader()
    for domain, count in sorted_dict.items():
        csv_writer.writerow({'domain': domain, 'count': count})
