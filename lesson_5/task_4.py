"""
Задание 4.
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы. Нужно обойтисть
без создания массива!
"""


def sum_el(count, sum_val=0):
    if count == 1:
        return sum_val + 1
    else:
        return sum_val + sum_el(count - 1, 1 / (2 ** (count - 1)))


print(f'Сумма элементов: {sum_el(int(input("Введите кол-во элементов: ")))}')
