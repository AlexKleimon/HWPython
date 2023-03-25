"""
Задание 1:
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: осень
Результат через словарь: осень
"""
number_month = int(input("Введите номер месяца (1...12): "))

# First method
my_lst = ["Зима", "Зима", "Весна", "Весна", "Весна",
          "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
if number_month == 1 or number_month == 2 or number_month == 12:
    print(f"Метод 1:\n{number_month} месяц -> {my_lst[number_month - 1]}")
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(f"Метод 1:\n{number_month} месяц -> {my_lst[number_month - 1]}")
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(f"Метод 1:\n{number_month} месяц -> {my_lst[number_month - 1]}")
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(f"Метод 1:\n{number_month} месяц -> {my_lst[number_month - 1]}")
else:
    print("ПОВТОРИТЕ ПОПЫТКУ! Всего 12 месяцев.")

# Second method
my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
           7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень",
           12: "Зима"}
try:
    print(f'Метод 2:\n{number_month} месяц -> {my_dict[number_month]}')
except KeyError:
    print("ПОВТОРИТЕ ПОПЫТКУ! Всего 12 месяцев.")
