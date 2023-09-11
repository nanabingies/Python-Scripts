# Paths in Graphs

'''
    Two vertices are adjacent when they are both incident to a common edge.

    A path in an undirected graph is a sequence of vertices P = ( v1, v2, ..., vn ) ∈ V x V x ... x V such that vi is adjacent to v{i+1} for 1 ≤ i < n. 
    Such a path P is called a path of length n from v1 to vn.

    A path with no repeated vertices is called a simple path.
'''

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
    
    def find_path(self, start_vertex: Any, end_vertex: Any, path: list = None) -> list:
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path is None:
            path = []

        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        
        if start_vertex not in graph:
            return None
        
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        
        return None
    
    def find_all_paths(self, start_vertex: Any, end_vertex: Any, path: list = []) -> list:
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        
        if start_vertex not in graph:
            return []
        
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths
    

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())


print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)

# ============================================================================================
print("\n\n\n")

g = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c", "f"},
      "e" : {"c"},
      "f" : {"a", "d"}
    }


graph = Graph(g)
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())


print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths("a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths("c", "c")
print(path)