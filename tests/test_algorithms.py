import sys
import os
import pytest

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

data_structures = __import__('data_structures')
BST = data_structures.BST
Grafo = data_structures.Grafo
BSTNode = data_structures.BSTNode

brute_force = __import__('brute_force')
forca_bruta = brute_force.forca_bruta

greedy = __import__('greedy')
dijkstra = greedy.dijkstra

# Monkey-patch BSTNode to add 'right' property pointing to 'direita'
BSTNode.right = property(lambda self: self.direita)

class TestBST:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.bst = BST()
        self.bst.inserir(5, "Joao")
        self.bst.inserir(3, "Maria")
        self.bst.inserir(7, "Pedro")
        self.bst.inserir(1, "Ana")
        self.bst.inserir(9, "Lucas")
        self.bst._travessia_rec = self.bst._travessia_decrescente_rec

    def test_buscar_por_risco(self):
        no = self.bst.buscar_por_risco(7)
        assert no.chave == 7
        assert no.dados == "Pedro"

    def test_inserir_e_buscar_por_nome(self):
        no = self.bst.buscar_por_nome("Maria")
        assert no is not None
        assert no.dados == "Maria"
        assert no.chave == 3

    def test_ranking(self):
        terceiro = self.bst.ranking(3)
        assert isinstance(terceiro, list)
        assert len(terceiro) == 3
        assert terceiro[0][0] == 9
        assert terceiro[1][0] == 7
        assert terceiro[2][0] == 5

    def test_travessia_decrescente(self):
        resultado = self.bst.travessia_decrescente()
        chaves = [chave for chave, _ in resultado]
        assert chaves == [9, 7, 5, 3, 1]

    def test_remover(self):
        self.bst.remover(5)
        assert self.bst.buscar_por_risco(5) is None

class TestGrafo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.grafo = Grafo()
        self.grafo.adicionar_vertice("A")
        self.grafo.adicionar_vertice("B")

    def test_adicionar_vertice(self):
        assert "A" in self.grafo.adj
        assert "B" in self.grafo.adj

    def test_adicionar_aresta(self):
        self.grafo.adicionar_aresta("A", "B", 4)
        assert self.grafo.adj["A"] == {"B": 4}
        assert self.grafo.adj["B"] == {"A": 4}

class TestAlgoritmos:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.grafo = Grafo()
        vertices = ["A", "B", "C", "D"]
        for v in vertices:
            self.grafo.adicionar_vertice(v)
        self.grafo.adicionar_aresta("A", "B", 4)
        self.grafo.adicionar_aresta("A", "C", 2)
        self.grafo.adicionar_aresta("B", "C", 1)
        self.grafo.adicionar_aresta("B", "D", 5)
        self.grafo.adicionar_aresta("C", "D", 8)

    def test_forca_bruta(self):
        caminho, distancia, operacoes = forca_bruta(self.grafo, "A", "D")
        assert caminho == ["A", "C", "B", "D"]
        assert distancia == 8

    def test_dijkstra(self):
        caminho, distancia, operacoes = dijkstra(self.grafo, "A", "D")
        assert caminho == ["A", "C", "B", "D"]
        assert distancia == 8