import random

def generate_adjacency_matrix(num_vertices):
    """
    Генерирует случайную матрицу смежности для графа с num_vertices вершинами.
    """
    matrix = [[random.randint(0, 1) for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        matrix[i][i] = 0  # Нет петель (ребер из вершины в саму себя)
    return matrix

def is_clique(graph, vertices):
    """
    Проверяет, является ли данное множество вершин кликой в графе.
    """
    for u in vertices:
        for v in vertices:
            if u != v and not graph[u][v]:
                return False
    return True

def brute_force_max_clique(graph):
    """
    Ищет максимальную клику в графе методом полного перебора.
    """
    n = len(graph)
    max_clique = []
    for i in range(1, 2**n):
        vertices = [v for v in range(n) if (i & (1 << v)) != 0]
        if is_clique(graph, vertices) and len(vertices) > len(max_clique):
            max_clique = vertices
    return max_clique

def N(vertex, graph):
    """
    Возвращает список соседей данной вершины.
    """
    return [i for i, val in enumerate(graph[vertex]) if val == 1]

def bronk(r, p, x, graph):
    """
    Рекурсивный алгоритм Брона-Кербоша.
    r: текущая клика
    p: кандидаты на добавление в клику
    x: исключенные вершины
    graph: матрица смежности графа
    """
    if not p and not x:
        print("Алгоритм Брона-Кербоша - максимальная клика:", r)  # Выводим максимальную клику
        return

    for vertex in p[:]:
        r_new = r + [vertex]
        p_new = [val for val in p if val in N(vertex, graph)]  # p пересекается с N(vertex)
        x_new = [val for val in x if val in N(vertex, graph)]  # x пересекается с N(vertex)
        bronk(r_new, p_new, x_new, graph)
        p.remove(vertex)
        x.append(vertex)

def local_search_max_clique(graph, max_iterations=1000):
    """
    Ищет приближенную максимальную клику с помощью метода локального поиска.
    """
    n = len(graph)
    current_clique = set(random.sample(range(n), min(10, n)))  # Начальная случайная клика
    best_clique = current_clique.copy()

    for _ in range(max_iterations):
        neighbors = set()
        for v in current_clique:
            neighbors |= set(graph[v])
        neighbors -= current_clique

        if not neighbors:
            break  # Нет соседей для улучшения

        # Попробуем добавить новую вершину
        new_vertex = random.choice(list(neighbors))
        new_clique = current_clique | {new_vertex}

        if len(new_clique) > len(current_clique):
            current_clique = new_clique

        if len(new_clique) > len(best_clique):
            best_clique = new_clique

    return list(best_clique)

def greedy_max_clique(graph):
    """
    Ищет приближенную максимальную клику с помощью жадного алгоритма.
    """
    n = len(graph)
    vertices = set(range(n))
    max_clique = set()
    while vertices:
        v = max(vertices, key=lambda x: len(vertices & set(graph[x])))
        max_clique.add(v)
        vertices &= set(graph[v])
    return list(max_clique)

def wilf_approx_max_clique(graph):
    """
    Приближенный алгоритм Уилфа для поиска максимальной клики в графе.
    """
    max_clique = set()
    vertices = set(graph.keys())

    while vertices:
        # Выбираем вершину с наибольшим числом соседей
        vertex = max(vertices, key=lambda v: len(graph[v]))
        max_clique.add(vertex)

        # Обновляем множество соседей
        vertices -= graph[vertex]

    return max_clique


# Получаем количество вершин от пользователя
num_vertices = int(input("Введите количество вершин в графе: "))
adj_matrix = generate_adjacency_matrix(num_vertices)

print("Сгенерированная матрица смежности:")
for row in adj_matrix:
    print(row)

print("Полный перебор - максимальная клика:", brute_force_max_clique(adj_matrix))
print("Алгоритм Брона-Кербоша:")
bronk([], list(range(num_vertices)), [], adj_matrix)
print("Приближенная максимальная клика - метод локального поиска:", local_search_max_clique(adj_matrix))
graph = {}
for i in range(num_vertices):
    graph[str(i)] = set(str(j) for j in range(num_vertices) if adj_matrix[i][j])
approx_max_clique = wilf_approx_max_clique(graph)
print("Приближенная максимальная клика - жадный алгоритм:", greedy_max_clique(adj_matrix))
print("Приближенная максимальная клика- алгоритм Уилфа:", approx_max_clique)





