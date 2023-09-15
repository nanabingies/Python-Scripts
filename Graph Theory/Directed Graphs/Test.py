import networkx as nx 
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'B')])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()

G = nx.cycle_graph(4, create_using=nx.DiGraph())
nx.add_cycle(G, [10, 11, 12])
[
    len(c)
    for c in sorted(nx.strongly_connected_components(G), key=len, reverse=True)
]