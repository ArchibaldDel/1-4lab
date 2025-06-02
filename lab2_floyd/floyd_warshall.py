# lab2_floyd/floyd_warshall.py

from typing import List
from lab1_amm.matrix import Matrix

INF = float('inf')


def floyd_warshall(adj_matrix: Matrix) -> Matrix:
    n = adj_matrix.rows
    # Копируем данные в новую матрицу
    dist = [row[:] for row in adj_matrix.data]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return Matrix(dist)


# Пример использования
if __name__ == "__main__":
    # INF означает отсутствие ребра (нет связи)
    a = Matrix([
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ])
    print("Исходная матрица смежности:")
    print(a)
    print("\nМатрица кратчайших расстояний (Floyd-Warshall):")
    result = floyd_warshall(a)
    print(result)
