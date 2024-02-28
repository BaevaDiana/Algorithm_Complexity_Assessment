import time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def count_nodes_recursive(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes_recursive(root.left) + self.count_nodes_recursive(root.right)

    def count_nodes_iterative(self, root):
        count = 0
        stack = [root]

        while stack:
            current_node = stack.pop()
            count += 1
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return count

if __name__ == "__main__":
    # Создаем простое бинарное дерево
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    # Измеряем время выполнения рекурсивного метода
    start_time_recursive = time.time()
    num_nodes_recursive = root.count_nodes_recursive(root)
    end_time_recursive = time.time()

    # Измеряем время выполнения итеративного метода
    start_time_iterative = time.time()
    num_nodes_iterative = root.count_nodes_iterative(root)
    end_time_iterative = time.time()

    print(f"Количество вершин в дереве (рекурсивно): {num_nodes_recursive}")
    print(f"Время выполнения (рекурсивно): {end_time_recursive - start_time_recursive:.6f} секунд")

    print(f"Количество вершин в дереве (итеративно): {num_nodes_iterative}")
    print(f"Время выполнения (итеративно): {end_time_iterative - start_time_iterative:.6f} секунд")
