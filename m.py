import time
import random
from collections import defaultdict

#Algoritmo Exato (Backtracking)
def cobertura_vertices_backtracking(G, k, cobertura=None, arestas_nao_cobertas=None, i=0):
    if cobertura is None:
        cobertura = set()
    if arestas_nao_cobertas is None:
        arestas_nao_cobertas = set(G)

    if k < 0 or i >= len(G):
        return None
    if not arestas_nao_cobertas:
        return cobertura

    u, v = list(G)[i]
    # Testar com o vértice u
    nova_cobertura = cobertura | {u}
    novas_arestas_nao_cobertas = {e for e in arestas_nao_cobertas if u not in e}
    cobertura_com_u = cobertura_vertices_backtracking(G, k - 1, nova_cobertura, novas_arestas_nao_cobertas, i + 1)

    if cobertura_com_u is not None:
        return cobertura_com_u

    # Testar com o vértice v apenas se necessário
    nova_cobertura = cobertura | {v}
    novas_arestas_nao_cobertas = {e for e in arestas_nao_cobertas if v not in e}
    return cobertura_vertices_backtracking(G, k - 1, nova_cobertura, novas_arestas_nao_cobertas, i + 1)

#Algoritmo Exato (Backtracking)

#Algoritmo de 2-Aproximação (Emparelhamento Máximo)
def emparelhamento_maximo(G):
    emparelhamento = set()
    visitado = set()
    for u, v in G:
        if u not in visitado and v not in visitado:
            emparelhamento.add((u, v))
            visitado.add(u)
            visitado.add(v)
    return emparelhamento

def cobertura_vertices_2aprox(G):
    emparelhamento = emparelhamento_maximo(G)
    return {v for edge in emparelhamento for v in edge}
#Algoritmo de 2-Aproximação (Emparelhamento Máximo)

#Heurística (Vértice de Maior Grau)
def escolhe_vertice_maior_grau(G):
    graus = defaultdict(int)
    for u, v in G:
        graus[u] += 1
        graus[v] += 1
    return max(graus, key=graus.get)

def cobertura_vertices_heuristica(G):
    cobertura = set()
    G_copia = G.copy()
    while G_copia:
        v = escolhe_vertice_maior_grau(G_copia)
        cobertura.add(v)
        G_copia = {e for e in G_copia if v not in e}
    return cobertura
#Heurística (Vértice de Maior Grau)

def gerar_grafo_aleatorio(n, probabilidadeAresta):
    """ Gera um grafo aleatório com n vértices e probabilidade p de aresta. """
    return {(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < probabilidadeAresta}

def testar_algoritmos(n, probabilidadeAresta):
    G = gerar_grafo_aleatorio(n, probabilidadeAresta)

    start1 = time.time()
    solucao_exata = cobertura_vertices_backtracking(G, n)
    tempo_exato = time.time() - start1
    tamanho_exato = len(solucao_exata) if solucao_exata is not None else "Não Encontrado"

    start2 = time.time()
    solucao_aprox = cobertura_vertices_2aprox(G)
    tempo_aprox = time.time() - start2

    start3 = time.time()
    solucao_heuristica = cobertura_vertices_heuristica(G)
    tempo_heuristica = time.time() - start3

    print(f"Tamanho do Grafo: {n}")
    print(f"Tempo (Backtracking): {tempo_exato}s")
    print(f"Tempo (Emparelhamento Máximo): {tempo_aprox}s")
    print(f"Tempo (Vértice de Maior Grau): {tempo_heuristica}s")
    print()
    


# Testar com diferentes tamanhos de grafos
for n in [5, 10, 15, 20, 21,22,23,24,25,26,50, 100, 1000, 2000]: #[10]: #
    testar_algoritmos(n, 1)
    