"""
Задача 26:
Напишите программу, которая на вход принимает два числа A и B, и
возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""


def degree_num(number_a, number_b):
    if number_b == 1:
        return number_a
    else:
        return number_a * degree_num(number_a, number_b - 1)


num_a = int(input("Введите число А: "))
num_b = int(input("Введите число B: "))
print(f"A: {num_a}, B: {num_b} -> {num_a}^{num_b} = "
      f"{degree_num(num_a, num_b)}")
