# -*- coding: utf-8 -*-
import heapq
from data_structures import Grafo

def dijkstra(grafo: Grafo, origem: str, destino: str):
    """
    Encontra o caminho mínimo utilizando o algoritmo de Dijkstra com fila de prioridades.
    Retorna (caminho, distancia, operacoes).
    """
    if origem not in grafo.adj or destino not in grafo.adj:
        return None, float('inf'), 0

    dist = {v: float('inf') for v in grafo.adj}
    dist[origem] = 0
    pai = {v: None for v in grafo.adj}
    
    pq = [(0, origem)]
    operacoes = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        operacoes += 1
        
        if u == destino:
            break
            
        if d > dist[u]:
            continue
            
        for v, peso in grafo.obter_vizinhos(u):
            operacoes += 1
            nova_dist = dist[u] + peso
            if nova_dist < dist[v]:
                dist[v] = nova_dist
                pai[v] = u
                heapq.heappush(pq, (nova_dist, v))
                
    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = pai[atual]
        
    if dist[destino] == float('inf'):
        return None, float('inf'), operacoes
        
    return caminho, dist[destino], operacoes


def dijkstra_priorizando_bst(grafo, bst, hubs, destino, top_k=3):
    """
    Usa a BST para consultar os municípios de maior risco,
    executa Dijkstra de cada hub até o destino,
    e retorna a melhor rota encontrada com o ranking de risco.
    """
    # 1. Usa a BST para consultar os top_k municípios de maior risco
    ranking_risco = bst.ranking(top_k)
    print(f"\n  🏆 Ranking de risco (BST):")
    for risco, municipio in ranking_risco:
        print(f"     - {municipio} (risco {risco})")
    
    # 2. Para cada município de alto risco, encontra a melhor rota
    melhor_rota = None
    melhor_dist = float('inf')
    
    for risco, municipio in ranking_risco:
        if municipio in hubs:
            caminho, dist, ops = dijkstra(grafo, municipio, destino)
            if caminho and dist < melhor_dist:
                melhor_rota = (municipio, caminho, dist, risco)
                melhor_dist = dist
    
    return melhor_rota


if __name__ == "__main__":
    print("=" * 50)
    print("Demonstração 1: Dijkstra padrão")
    print("=" * 50)
    
    g = Grafo()
    for v in ["A", "B", "C", "D", "E"]:
        g.adicionar_vertice(v)
        
    g.adicionar_aresta("A", "B", 4)
    g.adicionar_aresta("A", "C", 2)
    g.adicionar_aresta("B", "C", 1)
    g.adicionar_aresta("B", "D", 5)
    g.adicionar_aresta("C", "D", 8)
    g.adicionar_aresta("C", "E", 10)
    g.adicionar_aresta("D", "E", 2)

    caminho, distancia, operacoes = dijkstra(g, "A", "E")
    print(f"  ✅ Caminho ótimo: {caminho}")
    print(f"  📏 Distância: {distancia}")
    print(f"  ⚙️  Operações: {operacoes}")

    print("\n" + "=" * 50)
    print("Demonstração 2: BST + Dijkstra (acoplamento)")
    print("=" * 50)
    print("  A BST consulta municípios de alto risco para")
    print("  priorizar a ordem de execução do Dijkstra.\n")
    
    # Cria a BST com dados de risco
    from data_structures import BST
    bst = BST()
    bst.inserir(8, "Porto Alegre")
    bst.inserir(3, "Canoas")
    bst.inserir(10, "Eldorado do Sul")
    bst.inserir(1, "Guaíba")
    bst.inserir(6, "São Leopoldo")
    
    # Cria um grafo com os mesmos municípios
    g2 = Grafo()
    hubs = ["Porto Alegre", "Eldorado do Sul", "São Leopoldo"]
    destino = "Canoas"
    
    for v in hubs + [destino, "Guaíba"]:
        g2.adicionar_vertice(v)
    g2.adicionar_aresta("Porto Alegre", "Canoas", 15)
    g2.adicionar_aresta("Eldorado do Sul", "Porto Alegre", 20)
    g2.adicionar_aresta("São Leopoldo", "Canoas", 18)
    g2.adicionar_aresta("Porto Alegre", "Guaíba", 10)
    g2.adicionar_aresta("Guaíba", "Canoas", 12)
    
    resultado = dijkstra_priorizando_bst(g2, bst, hubs, destino)
    
    if resultado:
        hub_origem, caminho, dist, risco = resultado
        print(f"\n  ✅ Melhor rota encontrada:")
        print(f"     Origem: {hub_origem} (risco {risco} - prioritário via BST)")
        print(f"     Rota: {caminho}")
        print(f"     Distância: {dist}")
    else:
        print("  Nenhuma rota encontrada.")
    
    print("\n" + "=" * 50)
    print("Conclusão: A BST filtra os municípios críticos,")
    print("e o Dijkstra otimiza as rotas para esses alvos.")
    print("=" * 50)
