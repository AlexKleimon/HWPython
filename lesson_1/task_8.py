"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по прямой между
дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""
size_n = int(input('Введите размер стороны n шоколадки: '))
size_m = int(input('Введите размер стороны m шоколадки: '))
size_part = int(input('Введите количество долек: '))
if size_n * size_m > size_part and (
        size_part % size_n == 0 or size_part % size_m == 0):
    print(f"n = {size_n}, m = {size_m}, k = {size_part} -> yes")
else:
    print(f"n = {size_n}, m = {size_m}, k = {size_part} -> no")
