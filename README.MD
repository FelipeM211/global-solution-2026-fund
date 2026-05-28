# Global Solution 2026 — Economia Espacial

## Disciplina: Estruturas de Dados e Algoritmos
**Professor:** André Marques  
**Turma:** Engenharia de Software (3º Semestre)  
**Instituição:** FIAP  

---

## 👥 Integrantes do Grupo
*   **Nome:** Felipe B Murad - **RM:** 562347
*   **Nome:** Lucas Mesquita Massoni - **RM:** 561686

---

## 📌 Sobre o Projeto
Este projeto consiste em um sistema de monitoramento de riscos ambientais e otimização de rotas de transporte em municípios brasileiros. A solução integra estruturas de dados avançadas (Grafos e Árvores Binárias de Busca) com estratégias algorítmicas de Força Bruta e Gulosas para responder a desastres ecológicos.

### 🌍 Alinhamento com as ODS (ONU)
*   **ODS 2 (Fome Zero):** Otimização de rotas de distribuição de insumos e água no MATOPIBA para mitigar os impactos de secas severas.
*   **ODS 9 (Indústria, Inovação e Infraestrutura):** Desenvolvimento de algoritmos eficientes de roteamento e análise de redes de transporte.
*   **ODS 11 (Cidades Sustentáveis):** Planejamento de rotas de socorro e resposta rápida a enchentes no Rio Grande do Sul.
*   **ODS 13 (Ação Climática):** Classificação dinâmica e ordenação de índices de risco ambiental para tomada de decisão preventiva.

---

## 📂 Estrutura do Projeto
```text
GS_DYNAMIC_PROGRAMMING/
│
├── data/
│   ├── raw/                  # Dados brutos de entrada (NDVI, pluviometria)
│   └── processed/            # Grafos e árvores serializados (JSON/pickle)
│
├── src/
│   ├── data_structures.py    # Implementação da BST e do Grafo
│   ├── brute_force.py        # Algoritmo de Força Bruta (Backtracking DFS)
│   ├── greedy.py             # Algoritmo Guloso (Dijkstra com heapq)
│   ├── performance_monitor.py# Monitoramento de tempo, memória e operações
│   └── visualizations.py     # Renderização gráfica dos cenários com NetworkX
│
├── tests/
│   └──test_algorithms.py    # Suíte de testes unitários automatizados (pytest)
│
│
├── README.MD                 # Documentação do projeto (este arquivo)
└── requirements.txt          # Lista de dependências do Python

## 🛠️ Tecnologias e Dependências
O projeto utiliza as seguintes bibliotecas do ecossistema Python:
*   **NetworkX:** Para modelagem e manipulação matemática de estruturas de grafos complexas.
*   **Matplotlib:** Para renderização visual e plotagem interativa das redes de transporte.
*   **Pytest:** Para execução da suíte de testes unitários e validação de integridade.

---

## 🚀 Como Executar o Projeto

### 1. Instalar as Dependências
Abra o terminal na pasta raiz do projeto e execute:
```bash
pip install -r requirements.txt

### 2. Executar a Simulação Principal
Para rodar a simulação dos cenários, exibir os rankings de risco da BST, as métricas comparativas de desempenho (tempo, memória e operações) e abrir as janelas gráficas com as rotas destacadas em vermelho:
```bash
python GS.py

### 3. Executar os Testes Automatizados
Para rodar a suíte de testes unitários e garantir que todas as estruturas de dados e algoritmos estão funcionando perfeitamente:
```bash
pytest src/test_algorithms.py -v