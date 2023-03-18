"""
Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.
"""
number_N = int(input("Введите число N: "))
degree = 0
while 2 ** degree <= number_N:
    print(f"2^{degree} -> {2 ** degree}")
    degree += 1
