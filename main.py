import time
from collections import defaultdict
import plotly.graph_objects as go
import sys
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cobertura_vertices_backtracking(self, u, cobertura, k, visited):
        if k < 0:
            return None

        if u == self.V:
            if all(visited[v] or visited[u] for u in range(self.V) for v in self.graph[u]):
                return cobertura.copy()
            return None

        visited[u] = True
        solucao_sem_u = self.cobertura_vertices_backtracking(u + 1, cobertura, k, visited)
        if solucao_sem_u is not None:
            return solucao_sem_u

        visited[u] = False
        cobertura.add(u)
        solucao_com_u = self.cobertura_vertices_backtracking(u + 1, cobertura, k - 1, visited)
        if solucao_com_u is not None:
            return solucao_com_u

        cobertura.remove(u)
        return None

    def run_vertex_cover_backtracking(self):
        visited = [True] * self.V
        cobertura = self.cobertura_vertices_backtracking(0, set(), self.V, visited)
        return cobertura

    def emparelhamento_maximo(self):
        visitado = set()
        emparelhamento = []

        for u in range(self.V):
            if u not in visitado:
                for v in self.graph[u]:
                    if v not in visitado:
                        emparelhamento.append((u, v))
                        visitado.add(u)
                        visitado.add(v)
                        break
        return emparelhamento

    def cobertura_vertices_2aprox(self):
        emparelhamento = self.emparelhamento_maximo()
        return set(u for edge in emparelhamento for u in edge)

    def escolhe_vertice_maior_grau(self):
        graus = defaultdict(int)
        for u in range(self.V):
            for v in self.graph[u]:
                graus[u] += 1
                graus[v] += 1
        return max(graus, key=graus.get)

    def cobertura_vertices_heuristica(self):
        cobertura = set()
        while any(self.graph[u] for u in range(self.V)):
            v = self.escolhe_vertice_maior_grau()
            cobertura.add(v)
            for u in list(self.graph[v]):
                self.graph[u].remove(v)
                self.graph[v].remove(u)
        return cobertura

    def run_algorithms(self):
        start_time = time.time()
        cobertura_backtracking = self.run_vertex_cover_backtracking()
        tempo_backtracking = time.time() - start_time

        start_time = time.time()
        cobertura_2aprox = self.cobertura_vertices_2aprox()
        tempo_2aprox = time.time() - start_time

        start_time = time.time()
        cobertura_heuristica = self.cobertura_vertices_heuristica()
        tempo_heuristica = time.time() - start_time

        return {
            'backtracking': (cobertura_backtracking, tempo_backtracking),
            '2-aprox': (cobertura_2aprox, tempo_2aprox),
            'heuristica': (cobertura_heuristica, tempo_heuristica)
        }

def generate_graph_and_times():
    sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000, 20000, 50000, 100000]
    backtracking_times = []
    two_approx_times = []
    heuristic_times = []

    sys.setrecursionlimit(110000)

    for size in sizes:
        print(f"Tamanho do grafo: {size}")
        g = Graph(size)
        for i in range(size - 1):
            g.addEdge(i, i + 1)

        resultados = g.run_algorithms()

        for metodo, (cobertura, tempo) in resultados.items():
            print(f"Metodo: {metodo}, Tempo de execução: {tempo:.4f} segundos")

        backtracking_times.append(resultados['backtracking'][1])
        two_approx_times.append(resultados['2-aprox'][1])
        heuristic_times.append(resultados['heuristica'][1])

        print()

    return sizes, backtracking_times, two_approx_times, heuristic_times






sizes, backtracking_times, two_approx_times, heuristic_times = generate_graph_and_times()

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(sizes, backtracking_times, marker='o', label='Backtracking')
plt.plot(sizes, two_approx_times, marker='s', label='2-Aproximação (Emparelhamento Máximo)')
plt.plot(sizes, heuristic_times, marker='^', label='Heurística (Vértice de Maior Grau)')

plt.title('Comparação de Tempo de Execução dos Métodos por Tamanho do Grafo')
plt.xlabel('Tamanho do Grafo')
plt.ylabel('Tempo de Execução (segundos)')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()