# lab3_path/path_reconstruction.py

from typing import List, Optional
from lab1_amm.matrix import Matrix
from lab2_floyd.floyd_warshall import INF

def floyd_warshall_with_paths(adj_matrix: Matrix):
    n = adj_matrix.rows
    dist = [row[:] for row in adj_matrix.data]
    nxt = [[None if i == j or adj_matrix.data[i][j] == INF else j
            for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    return dist, nxt

def reconstruct_path(nxt: List[List[Optional[int]]], u: int, v: int) -> List[int]:
    if nxt[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        if u is None:
            return []
        path.append(u)
    return path

# Пример использования
if __name__ == "__main__":
    a = Matrix([
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ])
    dist, nxt = floyd_warshall_with_paths(a)
    u, v = 0, 3  # путь из 0 в 3
    path = reconstruct_path(nxt, u, v)
    print(f"Кратчайший путь из {u} в {v}: {path}")
    if path:
        length = dist[path[0]][path[-1]]
        print(f"Длина пути: {length}")
