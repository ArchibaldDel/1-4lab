# lab1_amm/main_matrix.py

from matrix import Matrix


def main():
    print("Демонстрация работы с матрицами")
    print("-" * 32)

    # Пример матриц
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])

    print("Матрица A:")
    print(a)
    print("\nМатрица B:")
    print(b)

    print("\nA + B =")
    print(a + b)

    print("\nA * B =")
    print(a * b)

    print("\nМатрица из нулей 3x2:")
    print(Matrix.zeros(3, 2))

    # Ввод из консоли (закомментировано по умолчанию)
    # print("\nВвод матрицы пользователем:")
    # c = Matrix.from_input()
    # print("Введенная матрица:")
    # print(c)


if __name__ == "__main__":
    main()
# main_matrix.py
