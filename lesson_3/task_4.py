"""
Задание 4:
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
используя функцию sort()
без функции sort()
"""


def my_func_sort(number_1, number_2, number_3):
    list_number = [number_1, number_2, number_3]
    list_number.sort()
    print(f"Метод с sort:\nНаибольшие два аргумента: {list_number[1]},"
          f" {list_number[2]}\nСумма: {list_number[1] + list_number[2]}")


def my_func(number_1, number_2, number_3):
    list_number = [number_1, number_2, number_3]
    for j in range(2):
        for i in range(1, 3):
            if list_number[i - 1] > list_number[i]:
                number_max = list_number[i - 1]
                list_number[i - 1] = list_number[i]
                list_number[i] = number_max
    print(f"Метод без sort:\nНаибольшие два аргумента: {list_number[1]},"
          f" {list_number[2]}\nСумма: {list_number[1] + list_number[2]}")


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
three_num = int(input("Введите третье число: "))
my_func(first_num, second_num, three_num)
my_func_sort(first_num, second_num, three_num)
