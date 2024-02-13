# скалярное умножение векторов

import random

def generate_random_vector(length):
    """Генерирует случайный вектор заданной длины с целыми числами."""
    return [random.randint(0, 100) for _ in range(length)]


def scalar_product(vector1, vector2):
    """Вычисляет скалярное произведение двух векторов."""
    if len(vector1) != len(vector2):
        raise ValueError("Векторы должны быть одинаковой длины")

    # Вычисляем скалярное произведение вручную
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


def main():
    try:
        length = int(input("Введите размерность векторов: "))
        vector1 = generate_random_vector(length)
        vector2 = generate_random_vector(length)

        scalar_result = scalar_product(vector1, vector2)
        print(f"Первый вектор: {vector1}")
        print(f"Второй вектор: {vector2}")
        print(f"Скалярное произведение: {scalar_result:}")
    except ValueError:
        print("Пожалуйста, введите целое число для размерности векторов.")


if __name__ == "__main__":
    main()
