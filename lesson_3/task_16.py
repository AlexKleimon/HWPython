"""
Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X
в массиве A [1..N]. Пользователь в первой строке вводит натуральное
число N - количество элементов в массиве. В последующих строках записаны
N целых чисел Ai. Последняя строка содержит число X.
Пример:
N = 5
1 2 3 4 5
3
-> 1
"""
import random

size_list = int(input("Введите длину массива: "))
list_numbers = []
print("Массив: ", end=' ')
for i in range(size_list):
    list_numbers.append(random.randint(0, 9))
    print(list_numbers[i], end=' ')
count_numb = int(input("\nВведите число, которое нужно проверить: "))
print(f"Количество повторений числа {count_numb} в массиве: "
      f"{list_numbers.count(count_numb)}")
