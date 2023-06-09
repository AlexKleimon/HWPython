"""
Задание 3.
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486, то надо
вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру. Пока все
числа не извлечены рекурсивные вызовы продолжаем Условие завершения рекурсии -
все цифры извлечены Используем операции % //.
Операции взятия по индексу применять нельзя. Решите через рекурсию.
В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def invert_number(number, num_str=""):
    if number == 0:
        return num_str
    else:
        num_str += str(number % 10)
        return invert_number(number // 10, num_str)


try:
    print(f'Перевернутое число: '
          f'{invert_number(int(input("Введите число: ")))}')
except RecursionError:
    print("Введите натуральное число.")
