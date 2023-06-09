"""
Задание 2.
Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру и смотреть
является ли она четной или нечетной. При этом увеличиваем соответствующий
счетчик. Пока все числа не извлечены, рекурсивные вызовы продолжаем.
Условие завершения рекурсии - все числа извлечены Используем операции % //.
Операции взятия по индексу применять нельзя. Решите через рекурсию. В задании
нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def count_numbers(number, count_even=0, count_odd=0):
    if number == 0:
        print(f"Количество четных и нечетных цифр в числе равно: "
              f"({count_even}, {count_odd})")
    else:
        if (number % 10) % 2 == 0:
            count_even += 1
            count_numbers(number // 10, count_even, count_odd)
        else:
            count_odd += 1
            count_numbers(number // 10, count_even, count_odd)


count_numbers(int(input("Введите число: ")))
