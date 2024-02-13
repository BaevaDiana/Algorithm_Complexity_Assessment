# сортировка массива (вставкой; выбором; пузырьковая)

import random

def generate_random_array(n):
    """Генерирует случайный массив целых чисел заданной длины."""
    return [random.randint(0, 100) for _ in range(n)]

def insertion_sort(arr):
    """Сортировка вставкой."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    """Сортировка выбором."""
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    """Сортировка пузырьком."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    try:
        n = int(input("Введите размерность массива: "))
        my_array = generate_random_array(n)

        print("Исходный массив:")
        print(my_array)

        # Копируем массив для каждой сортировки
        array_insertion = my_array.copy()
        array_selection = my_array.copy()
        array_bubble = my_array.copy()

        insertion_sort(array_insertion)
        selection_sort(array_selection)
        bubble_sort(array_bubble)

        print("\nОтсортированный массив (вставкой):")
        print(array_insertion)
        print("\nОтсортированный массив (выбором):")
        print(array_selection)
        print("\nОтсортированный массив (пузырьком):")
        print(array_bubble)
    except ValueError:
        print("Пожалуйста, введите целое число для размерности массива.")

if __name__ == "__main__":
    main()
