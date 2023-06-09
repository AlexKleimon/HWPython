"""
Задание 10.
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
number_coins = int(input("Введите количество монет: "))
count_zero = 0
count_one = 0
for i in range(number_coins):
    number_tails = int(input("0 - решка, все остальное - орел:"))
    if number_tails == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f"Нужно перевернуть {count_zero} решек.")
else:
    print(f"Нужно перевернуть {count_one} орлов.")
