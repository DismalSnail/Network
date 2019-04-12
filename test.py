import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([(1, 1, 1), (1, 1, 3)])

print(G.number_of_edges())
print(G.number_of_nodes())
