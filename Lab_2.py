import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# создаем граф
G = nx.Graph()
G.add_nodes_from(range(50))

# яма
for i in range(10):
    G.add_edge(i, i + 1)

# последовательность ребер от 19 до 36
for i in range(20, 36):
    G.add_edge(i - 1, i)
    G.add_edge(i, i + 1)

# Вниз, добавляем ребра между узлами от 36 до 49
for i in range(36, 49):
    G.add_edge(i, i + 1)

# центральность в собственных векторах
centrality = nx.eigenvector_centrality(G, max_iter=800)

# преобразование в массив
centrality_values = np.array(list(centrality.values()))

# график
plt.plot(centrality_values, marker='o')
plt.title('Centrality in eigenvectors for a custom graph')
plt.xlabel('Node index')
plt.ylabel('Eigenvector Centrality')
plt.grid()
plt.show()
