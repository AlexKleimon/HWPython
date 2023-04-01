"""
Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических операций допускаются
только +1 и -1. Также нельзя использовать циклы.
Пример:
2+2 = 4
"""


def sum_numbers(first, second):
    if first == 0:
        return second
    else:
        return sum_numbers(first - 1, second + 1)


number_a = int(input("Введите число A: "))
number_b = int(input("Введите число B: "))
print(f"{number_a} + {number_b} = {sum_numbers(number_a, number_b)}")
