# lab1_amm/matrix.py

from typing import List, Any

class Matrix:
    def __init__(self, data: List[List[Any]]):
        if not data or not data[0]:
            raise ValueError("Матрица не может быть пустой")
        row_len = len(data[0])
        for row in data:
            if len(row) != row_len:
                raise ValueError("Все строки должны быть одинаковой длины")
        self.data = [list(row) for row in data]
        self.rows = len(data)
        self.cols = row_len

    def __str__(self):
        return '\n'.join(' '.join(str(x) for x in row) for row in self.data)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения")
        result = []
        for i in range(self.rows):
            result.append([self.data[i][j] + other.data[i][j] for j in range(self.cols)])
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Число столбцов первой матрицы должно равняться числу строк второй")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(s)
            result.append(row)
        return Matrix(result)

    @staticmethod
    def zeros(rows: int, cols: int):
        return Matrix([[0 for _ in range(cols)] for _ in range(rows)])

    @staticmethod
    def from_input():
        print("Введите размеры матрицы (строки и столбцы):")
        rows, cols = map(int, input().split())
        print("Введите матрицу построчно (через пробел):")
        data = []
        for _ in range(rows):
            data.append(list(map(float, input().split())))
        return Matrix(data)
# matrix.py
