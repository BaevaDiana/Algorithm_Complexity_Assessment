# перемножение матриц (n x n)

import random

def generate_random_matrix(n):
    """Генерирует случайную матрицу размерности nxn с целочисленными значениями."""
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

def matrix_multiply(A, B):
    """Вычисляет произведение двух матриц."""
    n = len(A)
    p = len(B[0])
    m = len(B)

    # Создаем матрицу C размерности nxp, заполняем нулями
    C = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            # Вычисляем сумму произведений элементов A[i][k] и B[k][j]
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C

def main():
    try:
        n = int(input("Введите размерность матриц (n): "))
        matrix1 = generate_random_matrix(n)
        matrix2 = generate_random_matrix(n)

        result_matrix = matrix_multiply(matrix1, matrix2)
        print("Первая матрица:")
        for row in matrix1:
            print(row)
        print("\nВторая матрица:")
        for row in matrix2:
            print(row)
        print("\nРезультат умножения матриц:")
        for row in result_matrix:
            print(row)
    except ValueError:
        print("Пожалуйста, введите целое число для размерности матриц.")

if __name__ == "__main__":
    main()

