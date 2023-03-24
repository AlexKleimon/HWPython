"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
while 1:
    number_input = int(input('Введите целое трехзначное число:'))
    if 99 < number_input < 1000:
        break
    else:
        print('Вы ошиблись!')
number_one = number_input % 10
number_two = (number_input // 10) % 10
number_three = number_input // 100
print(f"{number_input} -> {number_one + number_two + number_three}"
      f" ({number_three} + {number_two} + {number_one})")
