"""
Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:

numbers — список целых чисел
start — целое неотрицательное число
end — целое неотрицательное число

Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно и возвращать полученный результат.
"""


def range_sum(numbers, start, end):
    if start == end:
        return numbers[end]
    return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
