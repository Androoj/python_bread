"""
Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
"""

import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for index_row in range(len(matrix)):
    random.shuffle(matrix[index_row])

print(matrix)
