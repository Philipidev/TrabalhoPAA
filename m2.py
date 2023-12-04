import time
from collections import defaultdict
import plotly.graph_objects as go
import sys  

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = defaultdict(list)  # Dicionário padrão para armazenar o grafo

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Adiciona para ambos os vértices porque o grafo é não direcionado

    def cobertura_vertices_backtracking(self, u, cobertura, k, visited):
        if k < 0:
            return None

        if u == self.V:  # Todos os vértices foram considerados
            if all(visited[v] or visited[u] for u in range(self.V) for v in self.graph[u]):
                return cobertura.copy()
            return None

        # Não incluir u na cobertura
        visited[u] = True
        solucao_sem_u = self.cobertura_vertices_backtracking(u + 1, cobertura, k, visited)
        if solucao_sem_u is not None:
            return solucao_sem_u

        # Incluir u na cobertura
        visited[u] = False
        cobertura.add(u)
        solucao_com_u = self.cobertura_vertices_backtracking(u + 1, cobertura, k - 1, visited)
        cobertura.remove(u)

        return solucao_com_u

    def run_vertex_cover_backtracking(self):
        start_time = time.time()
        visited = [True] * self.V
        cobertura = self.cobertura_vertices_backtracking(0, set(), self.V, visited)
        end_time = time.time()
        return cobertura, end_time - start_time
    
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
        cobertura_backtracking, tempo_backtracking = self.run_vertex_cover_backtracking()

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


def generate_graph():
    sizes = [100, 500, 1000, 2000, 2300]  # Tamanhos de grafos maiores podem levar muito tempo devido à natureza exponencial do algoritmo
    sys.setrecursionlimit(10000)  

    for size in sizes:
        print(f"Tamanho do grafo: {size}")
        g = Graph(size)

        # Adicionar arestas ao grafo
        for i in range(size - 1):
            g.addEdge(i, i + 1)

        # Executar algoritmos
        resultados = g.run_algorithms()

        # Exibir resultados
        for metodo, (cobertura, tempo) in resultados.items():
            # print(f"Metodo: {metodo}, Cobertura de Vértices: {cobertura}, Tempo de execução: {tempo:.4f} segundos")
            print(f"Metodo: {metodo}, Tempo de execução: {tempo} segundos")
        print()

if __name__ == '__main__':
    generate_graph()
