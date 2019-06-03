
import networkx as nx
from networkx.utils import accumulate
from networkx.utils import not_implemented_for
import numpy as np

__all__ = ['salience']


@not_implemented_for('directed')
@not_implemented_for('multigraph')
def _SPT(G, r, weight='weight'):

    G = G.copy()
    N = G.order()
    T = np.zeros((N, N))

    # Add the 'proximity' weight to each link (1/w) - WARNING: w has to be not zero!
    for i, j in G.edges():
        w = G[i][j][weight]
        G[i][j]['proximity'] = 1. / w

    paths = nx.shortest_path(G, source=r, weight='proximity')
    # each path is a dictionary with key: r and value:the list of nodes in the path

    # Filling T based on the presence of a link in at least one of the shortest paths
    for k, path in paths.items():
        for i in range(len(path) - 1):
            T[path[i]][path[i + 1]] = 1  # updating the matrix T because there is a link
    return T


def salience(G, weight='weight'):
    N = G.order()
    S = np.zeros((N, N))
    for n in G.nodes():
        S = S + _SPT(G, n, weight=weight)
    S = 1. * S / N
    return S
