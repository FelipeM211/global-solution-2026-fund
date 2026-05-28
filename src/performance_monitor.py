# -*- coding: utf-8 -*-
"""
FIAP - Engenharia de Software (3º Semestre)
Disciplina: Estruturas de Dados e Algoritmos
Estudante: Felipe B Murad

performance_monitor.py - Monitoramento de Desempenho
Seção 4 do edital: testes com N = 5, 8, 10, 12, 20, 50, 100 vértices.
"""

import time
import tracemalloc
import random
from data_structures import Grafo
from brute_force import forca_bruta
from greedy import dijkstra


def gerar_grafo(n_vertices):
    """Gera um grafo conectado com n_vertices para testes de desempenho."""
    g = Grafo()
    vertices = []

    for i in range(n_vertices):
        nome = chr(65 + i) if i < 26 else f"V{i}"
        vertices.append(nome)
        g.adicionar_vertice(nome)

    # Garante conexão: cadeia linear
    for i in range(n_vertices - 1):
        peso = random.randint(1, 10)
        g.adicionar_aresta(vertices[i], vertices[i + 1], peso)

    # Adiciona arestas extras aleatórias
    extras = 0
    while extras < n_vertices // 2:
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v and v not in g.adj.get(u, {}):
            peso = random.randint(1, 10)
            g.adicionar_aresta(u, v, peso)
            extras += 1

    return g, vertices[0], vertices[-1]


def medir(funcao, *args, **kwargs):
    """
    Mede tempo (milissegundos), memória (MB) e operações de uma função.
    Retorna (tempo_ms, memoria_mb, operacoes, caminho).
    """
    tracemalloc.start()
    inicio = time.perf_counter()
    resultado = funcao(*args, **kwargs)
    fim = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_ms = (fim - inicio) * 1000          # ms
    memoria_mb = peak / (1024 * 1024)         # MB
    caminho, distancia, operacoes = resultado  # (caminho, distancia, operacoes)

    return tempo_ms, memoria_mb, operacoes, caminho


if __name__ == '__main__':
    random.seed(42)
    tamanhos = [5, 8, 10, 12, 20, 50, 100]

    print("=" * 80)
    print("  MONITORAMENTO DE DESEMPENHO — Força Bruta vs Dijkstra")
    print("  Seção 4 do edital: N = 5, 8, 10, 12, 20, 50, 100 vértices")
    print("=" * 80)
    print(f"{'N':<6} {'Algoritmo':<20} {'Tempo (ms)':<18} {'Memória (MB)':<18} {'Operações':<12}")
    print("-" * 80)

    for N in tamanhos:
        g, orig, dest = gerar_grafo(N)

        # --- DIJKSTRA (roda para todos os tamanhos) ---
        tempo_ms, mem_mb, ops, caminho_d = medir(dijkstra, g, orig, dest)
        print(f"{N:<6} {'Dijkstra':<20} {tempo_ms:<18.4f} {mem_mb:<18.6f} {ops:<12}")

        # --- FORÇA BRUTA (apenas N <= 12) ---
        if N <= 12:
            try:
                tempo_ms2, mem_mb2, ops2, caminho_fb = medir(forca_bruta, g, orig, dest)
                print(f"{N:<6} {'Força Bruta':<20} {tempo_ms2:<18.4f} {mem_mb2:<18.6f} {ops2:<12}")

                # Validação cruzada
                if caminho_d != caminho_fb:
                    print(f"      ⚠️  DIFERENÇA! Dijkstra: {caminho_d} | FB: {caminho_fb}")
                else:
                    print(f"      ✅ Validação cruzada OK — caminhos idênticos")

            except Exception as e:
                print(f"{N:<6} {'Força Bruta':<20} {'--- erro ---':<18} {'':18} {'':<12}")
                print(f"      Erro: {e}")
        else:
            print(f"{N:<6} {'Força Bruta':<20} {'--- inviável ---':<18} {'':18} {'':<12}")

    print("-" * 80)
    print()
    print("  CONCLUSÃO DA ANÁLISE EMPÍRICA (Item 4):")
    print("  • Força Bruta: VIÁVEL até N = 12. A partir daí o crescimento")
    print("    fatorial O(N!) torna a execução proibitiva na prática.")
    print("  • Dijkstra: mantém tempo polinomial O((V+E) log V) para todos os N.")
    print("  • Cruzamento das curvas: ocorre entre N = 10 e N = 12.")
    print("  • Para N > 12: apenas Dijkstra é praticável.")
    print("=" * 80)