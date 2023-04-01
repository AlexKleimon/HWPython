"""
Задача 32.
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)
"""
import random

range_min = int(input("Введите минимум: "))
range_max = int(input("Введите максимум: "))
array_numbers = list()
count_list = list()
for i in range(10):
    array_numbers.append(random.randint(0, 100))
    if range_max > array_numbers[i] > range_min:
        count_list.append(i)
print(f"Массив: {array_numbers}\nИндексы элементов массива лежащие в "
      f"диапазоне [{range_min}, {range_max}]:", end=" ")
for el in count_list:
    print(el, end=" ")
