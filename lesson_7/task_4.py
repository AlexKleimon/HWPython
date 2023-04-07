"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц: 3 на 2,
3 на 3, 2 на 4.

31 22
37 43
51 86

 3  5 32
 2  4  6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица. Подсказка: сложение элементов матриц
выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, lst_matrix):
        self.lst_matrix = lst_matrix

    def __str__(self):
        matrix_str = ''
        for el in self.lst_matrix:
            for element in el:
                matrix_str += f"{element:3}"
            matrix_str += "\n"
        return matrix_str

    def __add__(self, other):
        res_matrix = []
        try:
            for i in range(len(self.lst_matrix)):
                for j in range(len(self.lst_matrix[i])):
                    res_matrix.append(
                        self.lst_matrix[i][j] + other.lst_matrix[i][j])
            return res_matrix
        except IndexError:
            print("Матрицы разных размеров.")


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_2)
print(matrix_2 + matrix_1)
