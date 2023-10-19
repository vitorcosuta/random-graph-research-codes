# Fazendo o carregamento dos dados do grafo. Repare que precisamos usar o modulo mmread do scipy para lermos o formato
# Matrix Market Exchange Format (.mtx), que eh o formato do nosso grafo.

from scipy.io import mmread
import networkx as nx

a = mmread('../network-repository/karate/soc-karate.mtx')
my_graph = nx.Graph(a)

# Importando a biblioteca matplot para plotar o grafo

import matplotlib.pyplot as plt

nx.draw(my_graph)
plt.draw()
plt.show()