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

    def count_nodes_recursive(self, root):
        """
        Рекурсивно подсчитывает количество вершин в бинарном упорядоченном дереве.
        :param root: Корень дерева
        :return: Количество вершин в дереве
        """
        if root is None:
            return 0
        return 1 + self.count_nodes_recursive(root.left) + self.count_nodes_recursive(root.right)

    def count_nodes_iterative(self, root):
        """
        Итеративно подсчитывает количество вершин в бинарном упорядоченном дереве.
        :return: Количество вершин в дереве
        """
        count = 0
        # стек для обхода дерева
        stack = [root]

        while stack:
            current_node = stack.pop()
            count += 1
            # добавление правого и левого потомков в стек (если они существуют)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return count

    def count_nodes_indirect(self):
        """
        Косвенно подсчитывает количество вершин в бинарном упорядоченном дереве.
        :return: Количество вершин в дереве
        """
        def count_recursive(node):
            if node is None:
                return 0
            return 1 + count_recursive(node.left) + count_recursive(node.right)

        return count_recursive(self)

if __name__ == "__main__":
    # создание простого бинарного дерева
    num_nodes = 50000
    root = TreeNode(None)
    root = root.create_random_tree(num_nodes)

    # измерение времени выполнения рекурсивного метода
    start_time_recursive = time.time()
    num_nodes_recursive = root.count_nodes_recursive(root)
    end_time_recursive = time.time()

    # измерение времени выполнения итеративного метода
    start_time_iterative = time.time()
    num_nodes_iterative = root.count_nodes_iterative(root)
    end_time_iterative = time.time()

    # измерение времени выполнения косвенной рекурсии
    start_time_indirect = time.time()
    num_nodes_indirect = root.count_nodes_indirect()
    end_time_indirect = time.time()

    print(f"Количество вершин в дереве (рекурсивно): {num_nodes_recursive}")
    print(f"Время выполнения (рекурсивно): {end_time_recursive - start_time_recursive:.9f} секунд")

    print(f"Количество вершин в дереве (итеративно): {num_nodes_iterative}")
    print(f"Время выполнения (итеративно): {end_time_iterative - start_time_iterative:.9f} секунд")

    print(f"Количество вершин в дереве (косвенно): {num_nodes_indirect}")
    print(f"Время выполнения (косвенная рекурсия): {end_time_indirect - start_time_indirect:.9f} секунд")