from scipy.io import mmread
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

a = mmread('../../network-repository/karate/soc-karate.mtx')
karate = nx.Graph(a)

# Graph.degree() retorna uma lista com tuplas (n,d), onde 'n' eh a numeracao do vertice e 'd' eh o grau do grafo
degree_sequence = sorted((d for n, d in karate.degree()), reverse=True)
dmax = max(degree_sequence)

fig = plt.figure("Graus do grafo Karate", figsize=(8, 8))
# Criando um gridspec para adicionar subplots de diferentes tamanhos
axgrid = fig.add_gridspec(5, 4)

ax0 = fig.add_subplot(axgrid[0:3, :])
pos = nx.spring_layout(karate, seed=10396953)
nx.draw_networkx_nodes(karate, pos, ax=ax0, node_size=20)
nx.draw_networkx_edges(karate, pos, ax=ax0, alpha=0.4)
ax0.set_title("Componetes conectados de Karate")
ax0.set_axis_off()

fig.tight_layout()
plt.show()