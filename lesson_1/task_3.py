"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number_n = input(f'Введите целое положительное число n: ')
sum_numbers = int(number_n) + int(number_n + number_n) + int(
    number_n + number_n + number_n)
print(f"n + nn + nnn = {sum_numbers}")
