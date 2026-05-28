# -*- coding: utf-8 -*-
"""
FIAP - Engenharia de Software (3º Semestre)
Disciplina: Estruturas de Dados e Algoritmos
Estudante: Felipe B Murad

brute_force.py - Algoritmo de Força Bruta (Backtracking DFS com Poda)
Alinhamento com as ODS da ONU:
- ODS 9 (Indústria, Inovação e Infraestrutura): Análise de caminhos ótimos absolutos.
"""

from data_structures import Grafo

def forca_bruta(grafo: Grafo, origem: str, destino: str):
    """
    Realiza uma busca exaustiva em profundidade (DFS) para encontrar o caminho mínimo.
    Retorna (melhor_caminho, melhor_distancia, operacoes).
    """
    melhor_caminho = None
    melhor_distancia = float('inf')
    operacoes = 0
    
    # Pilha para DFS iterativo com backtracking
    # Estrutura: (vertice_atual, caminho_percorrido, distancia_acumulada)
    pilha = [(origem, [origem], 0)]
    
    while pilha:
        vertice, caminho, distancia = pilha.pop()
        operacoes += 1  # Incrementa operação a cada nó processado
        
        if vertice == destino:
            if distancia < melhor_distancia:
                melhor_distancia = distancia
                melhor_caminho = caminho
            continue
            
        # PODA: Se a distância atual já é pior que a melhor encontrada, interrompe este ramo
        if distancia >= melhor_distancia:
            continue
            
        for vizinho, peso in grafo.obter_vizinhos(vertice):
            operacoes += 1  # Incrementa operação a cada vizinho avaliado
            if vizinho not in caminho:  # Evita ciclos na rota
                pilha.append((vizinho, caminho + [vizinho], distancia + peso))
                
    return melhor_caminho, melhor_distancia, operacoes

if __name__ == "__main__":
    # Importação local apenas para o teste manual
    from data_structures import Grafo

    print("="*40)
    print("Iniciando teste manual da Força Bruta...")
    print("="*40)
    
    # 1. Criando um grafo de exemplo
    g = Grafo()
    for v in ["A", "B", "C", "D"]:
        g.adicionar_vertice(v)
        
    g.adicionar_aresta("A", "B", 4)
    g.adicionar_aresta("A", "C", 2)
    g.adicionar_aresta("B", "C", 1)
    g.adicionar_aresta("B", "D", 5)
    g.adicionar_aresta("C", "D", 8)

    print("Grafo criado com sucesso!")
    print("Buscando o menor caminho de 'A' para 'D'...\n")

    # 2. Executando o algoritmo
    caminho, distancia, operacoes = forca_bruta(g, "A", "D")
    
    # 3. Imprimindo os resultados no terminal
    print(f"✅ Caminho ótimo encontrado: {caminho}")
    print(f"📏 Distância total: {distancia}")
    print(f"⚙️ Operações realizadas (nós visitados): {operacoes}")
    print("="*40)