from lab1_amm.matrix import Matrix
from lab2_floyd.floyd_warshall import floyd_warshall, INF
from lab3_path.path_reconstruction import floyd_warshall_with_paths, reconstruct_path
from lab4_parallel.cannon import cannon_multiply

def main():
    print("1. Демонстрация Matrix")
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    print("A:\n", A)
    print("B:\n", B)
    print("A + B:\n", A + B)
    print("A * B:\n", A * B)

    print("\n2. Флойд–Уоршел")
    g = Matrix([
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ])
    fw_result = floyd_warshall(g)
    print("Кратчайшие расстояния:\n", fw_result)

    print("\n3. Восстановление пути")
    dist, nxt = floyd_warshall_with_paths(g)
    u, v = 0, 3
    path = reconstruct_path(nxt, u, v)
    print(f"Кратчайший путь из {u} в {v}: {path}")

    print("\n4. Кэнон (распараллеливание умножения)")
    C = cannon_multiply(A, B)
    print("A * B (Cannon):\n", C)

if __name__ == "__main__":
    main()
