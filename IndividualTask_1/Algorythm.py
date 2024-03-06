import random
import time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def create_random_tree(self, num_nodes):
        """
        Создает случайное бинарное упорядоченное дерево с заданным количеством вершин.
        Значения вершин генерируются случайно в диапазоне от 1 до 100.
        :param num_nodes: Количество вершин в дереве
        :return: Корень дерева
        """
        def insert_node(root, value):
            if root is None:
                return TreeNode(value)
            if value < root.value:
                root.left = insert_node(root.left, value)
            else:
                root.right = insert_node(root.right, value)
            return root

        root = None
        for _ in range(num_nodes):
            value = random.randint(1, 100)  # генерируем случайное значение
            root = insert_node(root, value)

        return root

    def find_next_key_recursive(self, root, key):
        """
        Рекурсивно находит следующий ключ в бинарном дереве по отношению к заданному ключу.
        :param root: Корень дерева для поиска
        :param key: Заданный ключ
        :return: Следующий ключ или None, если такого нет
        """
        if root is None:
            return None

        if root.value <= key:
            return self.find_next_key_recursive(root.right, key)
        else:
            left = self.find_next_key_recursive(root.left, key)
            return root.value if left is None else left

    def find_next_key_iterative(self, key):
        """
        Находит следующий ключ в бинарном дереве по отношению к заданному ключу.
        :param key: Заданный ключ
        :return: Следующий ключ или None, если такого нет
        """
        current = self
        successor = None

        while current is not None:
            if current.value <= key:
                current = current.right
            else:
                successor = current.value
                current = current.left

        return successor


if __name__ == "__main__":
    # создание простого бинарного дерева
    num_nodes = 10000
    root = TreeNode(None)
    root = root.create_random_tree(num_nodes)

    # измерение времени выполнения рекурсивного метода
    start_time_recursive = time.time()
    target_key = random.randint(1, 100)
    next_key_1 = root.find_next_key_recursive(root,target_key)
    end_time_recursive = time.time()

    # измерение времени выполнения итеративного метода
    start_time_iterative = time.time()
    next_key_2 = root.find_next_key_iterative(target_key)
    end_time_iterative = time.time()

    print(f"Заданный ключ: {target_key}, следующий ключ: {next_key_1}")
    print(f"Время выполнения (рекурсивно): {end_time_recursive - start_time_recursive:.10f} секунд")

    print(f"Заданный ключ: {target_key}, следующий ключ: {next_key_2}")
    print(f"Время выполнения (итеративно): {end_time_iterative - start_time_iterative:.10f} секунд")
