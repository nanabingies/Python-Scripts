""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

from typing import TypeVar, Any
from collections import defaultdict

T = TypeVar("T")

class Graph(object):
    _graph_dict: dict = defaultdict(None)
    _iter_obj: iter

    def __init__(self, graph_dict: dict[T] = None) -> None:
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice: T) -> list:
        """ returns a list of all the edges of a vertice """
        return self._graph_dict[vertice]
    
    def all_vertices(self) -> set:
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())
    
    def all_edges(self) -> list:
        """ returns the edges of a graph """
        return self.__generate_edges()
    
    def add_vertex(self, vertex: T) -> None:
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge: T) -> None:
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
            Append edges to a vertex
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)

        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self) -> list:
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbor in self._graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})

        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)
    
    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge)

        return res
    

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

graph = Graph(g)
for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

graph.add_edge({"ab", "fg"})
graph.add_edge({"xyz", "bla"})
print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("Add vertex:")
graph.add_vertex("z")

print("Add an edge:")
graph.add_edge({"a", "d"})

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())