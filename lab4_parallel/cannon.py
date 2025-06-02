# lab4_parallel/cannon.py

from lab1_amm.matrix import Matrix
from typing import List
import threading

def shift_row_left(row: List, steps: int) -> List:
    n = len(row)
    return row[steps:] + row[:steps]

def shift_col_up(matrix: List[List], col: int, steps: int) -> None:
    n = len(matrix)
    col_values = [matrix[i][col] for i in range(n)]
    col_values = col_values[steps:] + col_values[:steps]
    for i in range(n):
        matrix[i][col] = col_values[i]

def cannon_multiply(A: Matrix, B: Matrix) -> Matrix:
    """Классический алгоритм Кэнона для квадратных матриц."""
    n = A.rows
    # Создаем копии данных
    a = [row[:] for row in A.data]
    b = [row[:] for row in B.data]
    c = [[0] * n for _ in range(n)]

    # Начальные сдвиги
    for i in range(n):
        a[i] = shift_row_left(a[i], i)
    for j in range(n):
        shift_col_up(b, j, j)

    # Основной цикл
    for step in range(n):
        # Параллельно — имитируется, на практике можно сделать через threading.Thread
        threads = []
        for i in range(n):
            for j in range(n):
                def add_to_c(ii=i, jj=j):
                    c[ii][jj] += a[ii][jj] * b[ii][jj]
                t = threading.Thread(target=add_to_c)
                threads.append(t)
                t.start()
        for t in threads:
            t.join()
        # Сдвигаем строки и столбцы для следующей итерации
        for i in range(n):
            a[i] = shift_row_left(a[i], 1)
        for j in range(n):
            shift_col_up(b, j, 1)
    return Matrix(c)

# Пример использования
if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    print("A:")
    print(A)
    print("\nB:")
    print(B)
    print("\nA * B (Cannon):")
    C = cannon_multiply(A, B)
    print(C)
