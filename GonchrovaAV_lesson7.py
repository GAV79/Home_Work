# задача 1
""" Вариант задачи, когда матрица генерируется из случайных чисел,
но в этом варианте не смогла реализовать суммирование по элементам,
так как параметры здесь - это число строк и столбцов, а не сами элементы. """

from random import randint


class Matrix:
    def __init__(self, row, column):  # передаем число строк и столбцов в матрице
        self.row = row
        self.column = column
        self.matrix = []
        for el in range(1, self.row + 1):
            matrix_tochter = []
            count = 0
            while count < self.column:
                a = randint(10, 99)
                matrix_tochter.append(a)
                count += 1
            self.matrix.append(matrix_tochter)
        print(self)
        print(self.matrix)
        self.pr()

    def pr(self):
        for li in self.matrix:
            for el in li:
                print(f'| {el} | ', end="")
            print()

    def __str__(self):
        return f'Матрица: строк: {self.row}; столбцов: {self.column}'


matrix1 = Matrix(2, 2)
matrix2 = Matrix(2, 2)

# задача 1
"""Решение задачи по условию"""


class Matrix:

    def __init__(self, ar1, ar2, ar3, ar4):
        self.ar1 = ar1
        self.ar2 = ar2
        self.ar3 = ar3
        self.ar4 = ar4
        self.matrix = [[ar1, ar2], [ar3, ar4]]

    def __str__(self):
        return f'Матрица:\n{self.ar1} | {self.ar2}\n{self.ar3} | {self.ar4}'

    def __add__(self, other):
        return f'Новая матрица:\n{self.ar1 + other.ar1} | {self.ar2 + other.ar2}\n' \
               f'{self.ar3 + other.ar3} | {self.ar4 + other.ar4}'


mtr1 = Matrix(2, 8, 3, 5)
print(mtr1)
mtr2 = Matrix(8, 2, 7, 5)
print(mtr2)
print(mtr1 + mtr2)

# Задача 2


from abc import ABC, abstractmethod


class Cloth(ABC):
    ras_tk = 0

    @abstractmethod
    def tk(self):
        pass


class Palto(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def tk(self):
        ras_tk = self.size / 6.5 + 0.5
        Cloth.ras_tk += ras_tk
        return f'Расход ткани на пальто = {round(ras_tk, 2)}'


class Kostum(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def tk(self):
        ras_tk = self.height * 2 + 0.3
        Cloth.ras_tk += ras_tk
        return f'Расход ткани на костюм = {round(ras_tk, 2)}'


a = Palto(53)
print(a.tk)
b = Kostum(1.6)
print(b.tk)
print(f'Общий расчет ткани = {round(Cloth.ras_tk, 2)}')


# Задача 3
class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return f'Число ячеек при сложении равно {self.num + other.num}'

    def __sub__(self, other):
        if self.num - other.num > 0:
            return f'Число ячеек при вычитании равно {self.num - other.num}'
        else:
            return f'Клетки не вычитаются'

    def __mul__(self, other):
        return f'Число ячеек при произведении равно {self.num * other.num}'

    def __truediv__(self, other):
        return f'Число ячеек при делении равно {int(self.num / other.num)}'

    def make_order(self, n_row):
        row = ''
        b = self.num // n_row
        d = self.num - b * n_row
        for el in range(1, b + 1):
            row += '*' * n_row + '\n'
        row += "*" * d
        print(row)


a1 = Cell(9)
a2 = Cell(4)
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
a1.make_order(2)
