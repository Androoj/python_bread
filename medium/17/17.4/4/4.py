"""
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом).
Оценка - целое число от 0 до 100 включительно.

Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.
"""

with open('class_scores.txt', encoding='utf-8') as file, open('new_scores.txt', 'w', encoding='utf-8') as new_file:

    for row in file:
        name, score = row.split()
        print(name, score)
        score = '100' if int(score) + 5 > 100 else str(int(score) + 5)
        new_file.write(f'{name} {score}\n')
