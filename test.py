import networkx as nx

G = nx.path_graph(4)
centrality = nx.eigenvector_centrality(G)
sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())
print("s")
