"""
Задача 18:
Требуется найти в массиве A [1...N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное
число N - количество элементов в массиве. В последующих строках
записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
N = 5
1 2 3 4 5
6
-> 5
"""
import random


def print_array(lst_numbers):
    print("Массив: ", end=' ')
    for i in lst_numbers:
        print(i, end=' ')


def search_number(*args):
    lst_numbers = args[0]
    num_x = args[1]
    min_diff_numbers = abs(num_x - lst_numbers[0])
    index = 0
    index_2 = -1
    for i in range(1, size_list):
        diff_numbers = abs(num_x - lst_numbers[i])
        if min_diff_numbers > diff_numbers != 0:
            min_diff_numbers = diff_numbers
            index = i
        elif (min_diff_numbers == diff_numbers and
              lst_numbers[i] != lst_numbers[index]):
            # Проверить на наличие второго близкого элемента числа number_x
            index_2 = i
    if index_2 != -1:
        print(f"Числу {num_x} близки два числа по величине:"
              f" {lst_numbers[index]} и {lst_numbers[index_2]}")
    else:
        print(f"Самое близкое по величине число: {lst_numbers[index]}")


size_list = int(input("Введите длину массива: "))
list_numbers = [random.randint(0, 9) for i in range(size_list)]
print_array(list_numbers)
number_x = int(input("\nВведите число X: "))
search_number(list_numbers, number_x)
