# -*- coding: utf-8 -*-
class BSTNode:
    """Nó da Árvore Binária de Busca (BST)."""
    def __init__(self, chave, dados):
        self.chave = chave          # Índice de risco ambiental (chave de ordenação)
        self.dados = dados          # Nome do município ou informações adicionais
        self.esquerda = None
        self.direita = None


class BST:
    """Árvore Binária de Busca para ordenação e ranking de riscos ambientais."""
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, dados):
        """Insere um novo nó na BST de forma ordenada."""
        if self.raiz is None:
            self.raiz = BSTNode(chave, dados)
        else:
            self._inserir_rec(self.raiz, chave, dados)

    def _inserir_rec(self, node, chave, dados):
        if chave < node.chave:
            if node.esquerda is None:
                node.esquerda = BSTNode(chave, dados)
            else:
                self._inserir_rec(node.esquerda, chave, dados)
        else:
            if node.direita is None:
                node.direita = BSTNode(chave, dados)
            else:
                self._inserir_rec(node.direita, chave, dados)

    def buscar_por_nome(self, nome):
        """Busca um município na árvore pelo nome (busca exaustiva O(N))."""
        return self._buscar_nome_rec(self.raiz, nome)

    def _buscar_nome_rec(self, node, nome):
        if node is None:
            return None
        if node.dados == nome:
            return node
        
        esquerda = self._buscar_nome_rec(node.esquerda, nome)
        if esquerda:
            return esquerda
        return self._buscar_nome_rec(node.direita, nome)

    def buscar_por_risco(self, risco):
        """Busca eficiente na BST pelo índice de risco (O(log N))."""
        return self._buscar_risco_rec(self.raiz, risco)

    def _buscar_risco_rec(self, node, risco):
        if node is None or node.chave == risco:
            return node
        if risco < node.chave:
            return self._buscar_risco_rec(node.esquerda, risco)
        return self._buscar_risco_rec(node.direita, risco)

    # ==================== NOVO MÉTODO 1 ====================
    def buscar_por_intervalo(self, r_min, r_max):
        """
        Retorna todos os municípios com índice de risco no intervalo [r_min, r_max].
        Complexidade O(K + log N), onde K é o número de resultados encontrados.
        O log N vem da descida até o primeiro nó relevante; K é a coleta linear.
        """
        resultado = []
        self._buscar_intervalo_rec(self.raiz, r_min, r_max, resultado)
        return resultado

    def _buscar_intervalo_rec(self, node, r_min, r_max, resultado):
        """Percorre a BST em ordem, coletando nós dentro do intervalo."""
        if node is None:
            return
        
        # Se o mínimo é menor que a chave atual, pode haver nós na esquerda
        if r_min < node.chave:
            self._buscar_intervalo_rec(node.esquerda, r_min, r_max, resultado)
        
        # Se a chave atual está dentro do intervalo, adiciona
        if r_min <= node.chave <= r_max:
            resultado.append((node.chave, node.dados))
        
        # Se o máximo é maior que a chave atual, pode haver nós na direita
        if r_max > node.chave:
            self._buscar_intervalo_rec(node.direita, r_min, r_max, resultado)
    # =======================================================

    def remover(self, chave):
        """Remove um nó da BST a partir de sua chave de risco."""
        self.raiz = self._remover_rec(self.raiz, chave)

    def _remover_rec(self, node, chave):
        if node is None:
            return node

        if chave < node.chave:
            node.esquerda = self._remover_rec(node.esquerda, chave)
        elif chave > node.chave:
            node.direita = self._remover_rec(node.direita, chave)
        else:
            # Caso 1: Nó folha ou com apenas um filho
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda

            # Caso 2: Nó com dois filhos (obter o sucessor in-order)
            sucessor = self._min_valor_node(node.direita)
            node.chave = sucessor.chave
            node.dados = sucessor.dados
            node.direita = self._remover_rec(node.direita, sucessor.chave)

        return node

    def _min_valor_node(self, node):
        """Retorna o nó de menor chave a partir de um nó dado."""
        atual = node
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    # ==================== NOVO MÉTODO 2 ====================
    def altura(self):
        """
        Calcula a altura da árvore (número de arestas no maior caminho
        da raiz até a folha mais distante).
        Altura de árvore vazia: -1.
        Altura de nó folha: 0.
        Útil para avaliar o balanceamento da BST.
        """
        return self._altura_rec(self.raiz)

    def _altura_rec(self, node):
        if node is None:
            return -1
        return 1 + max(self._altura_rec(node.esquerda), self._altura_rec(node.direita))
    # =======================================================

    def travessia_decrescente(self):
        """Retorna uma lista ordenada decrescentemente de tuplas (risco, município)."""
        elementos = []
        self._travessia_decrescente_rec(self.raiz, elementos)
        return elementos

    def _travessia_decrescente_rec(self, node, elementos):
        if node is not None:
            self._travessia_decrescente_rec(node.direita, elementos)
            elementos.append((node.chave, node.dados))
            self._travessia_decrescente_rec(node.esquerda, elementos)

    def ranking(self, k):
        """Retorna os top-k municípios com maior índice de risco."""
        elementos = self.travessia_decrescente()
        return elementos[:k]


class Grafo:
    """Grafo não direcionado representado por Lista de Adjacência."""
    def __init__(self):
        self.adj = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo."""
        if vertice not in self.adj:
            self.adj[vertice] = {}

    def adicionar_aresta(self, u, v, peso):
        """Adiciona uma aresta ponderada e não direcionada entre u e v."""
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adj[u][v] = peso
        self.adj[v][u] = peso

    def obter_vizinhos(self, vertice):
        """Retorna a lista de vizinhos e seus pesos para o vértice informado."""
        return list(self.adj.get(vertice, {}).items())


if __name__ == "__main__":
    print("=" * 40)
    print("Testando Árvore Binária de Busca (BST)")
    print("=" * 40)
    bst = BST()
    bst.inserir(8, "Porto Alegre")
    bst.inserir(3, "Canoas")
    bst.inserir(10, "Eldorado do Sul")
    bst.inserir(1, "Guaíba")
    bst.inserir(6, "São Leopoldo")
    
    print("Ranking dos 3 municípios com maior risco:")
    for risco, municipio in bst.ranking(3):
        print(f"  - {municipio} (Risco: {risco})")

    print("\nBuscando por intervalo de risco entre 5 e 11:")
    for risco, municipio in bst.buscar_por_intervalo(5, 11):
        print(f"  - {municipio} (Risco: {risco})")

    print(f"\nAltura da BST: {bst.altura()}")
        
    print("\nRemovendo município com risco 3 (Canoas)...")
    bst.remover(3)
    
    print("Novo ranking completo (decrescente):")
    for risco, municipio in bst.travessia_decrescente():
        print(f"  - {municipio} (Risco: {risco})")

    print("\n" + "=" * 40)
    print("Testando Grafo de Municípios")
    print("=" * 40)
    g = Grafo()
    g.adicionar_aresta("Porto Alegre", "Canoas", 15)
    g.adicionar_aresta("Porto Alegre", "Eldorado do Sul", 20)
    g.adicionar_aresta("Canoas", "São Leopoldo", 18)
    
    print("Vizinhos de Porto Alegre:")
    for vizinho, distancia in g.obter_vizinhos("Porto Alegre"):
        print(f"  - {vizinho} ({distancia} km)")
    print("=" * 40)
