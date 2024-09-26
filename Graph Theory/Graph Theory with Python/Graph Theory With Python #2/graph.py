# G = (V, E)
from collections import namedtuple
from platform import node

Graph = namedtuple('Graph', ['nodes', 'edges', 'is_directed'])

nodes = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B'),
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'C'),
    ('A', 'D'),
    ('B', 'D'),
    ('C', 'D'),
]

G = Graph(nodes, edges)


def adjacency_dict(graph: Graph):
    """_summary_

    Args:
        graph (Graph): _description_

    Returns the adjacency list representation of the graph.
    """
    adj = { node: [] for node in graph.nodes }
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj

def adjacency_matrix(graph: Graph):
    """_summary_

    Args:
        graph (Graph): _description_

    Returns the adjacency matrix of the graph
    
    Assumes that graph.nodes is equivalent to range(len(graph.nodes))
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj
