import numpy as np


def dijkstra(graph, start_vertex):

    n = len(graph)  # количество вершин в графе
    visited = [False] * n  # массив для отслеживания посещенных вершин
    # массив расстояний, инициализация бесконечностью
    distances = [float('inf')] * n
    distances[start_vertex] = 0  # расстояние до стартовой вершины равно 0

    for _ in range(n):
        # Находим вершину с минимальным расстоянием
        min_distance = float('inf')
        min_vertex = None
        for vertex in range(n):
            # рассматривается только непосещенная вершина и кратчайшие пути
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:  # Если все вершины посещены или несовершенные
            break

        visited[min_vertex] = True  # Помечаем вершину как посещенную

        # Обновляем расстояния
        for neighbor in range(n):
            if graph[min_vertex][neighbor] > 0:  # Проверяем наличие ребра
                distance = distances[min_vertex] + graph[min_vertex][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances


# Пример графа в виде матрицы смежности
graph = np.array([
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
])

start_vertex = 1  # начальная вершина
distances = dijkstra(graph, start_vertex)  # вызываем алгоритм

print("Кратчайшие расстояния от вершины", start_vertex, ":")
for i in range(len(distances)):
    print(f"До вершины {i}: {distances[i]}")
