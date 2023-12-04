# README para o Código de Comparação de Algoritmos de Cobertura de Vértices

## Descrição
Este código é projetado para comparar a eficiência de três diferentes algoritmos de cobertura de vértices em grafos: Backtracking, 2-Aproximação e Heurística de Vértice de Maior Grau. A eficácia é medida com base no tempo de execução ao processar grafos de diferentes tamanhos.

## Requisitos
- Python 3
- Bibliotecas: `matplotlib`, `plotly`, `collections`

## Instalação
Certifique-se de que o Python 3 e as bibliotecas necessárias estejam instalados. Se não estiverem, você pode instalá-los usando pip:

```bash
pip install matplotlib plotly
```

## Uso
Para executar o script, simplesmente rode o arquivo Python. O script gera grafos de tamanhos variados e aplica os três métodos de cobertura de vértices. Os tempos de execução são coletados e exibidos em um gráfico para comparação.

```bash
python nome_do_arquivo.py
```

## Estrutura do Código

### Classe `Graph`
Define um grafo e inclui métodos para adicionar arestas e calcular a cobertura de vértices usando diferentes algoritmos.

#### Métodos Principais:
- `addEdge(u, v)`: Adiciona uma aresta ao grafo.
- `cobertura_vertices_backtracking(...)`: Implementa o método de backtracking.
- `emparelhamento_maximo()`: Encontra um emparelhamento máximo para a 2-aproximação.
- `cobertura_vertices_2aprox()`: Implementa o método de 2-aproximação.
- `escolhe_vertice_maior_grau()`: Escolhe um vértice de maior grau para a heurística.
- `cobertura_vertices_heuristica()`: Implementa o método heurístico.
- `run_algorithms()`: Executa todos os métodos e coleta os tempos de execução.

### Função `generate_graph_and_times()`
Gera grafos de diferentes tamanhos e aplica os algoritmos de cobertura de vértices, coletando os tempos de execução.

### Plotagem de Gráfico
O script usa `matplotlib` para plotar os tempos de execução dos três métodos em relação ao tamanho dos grafos.