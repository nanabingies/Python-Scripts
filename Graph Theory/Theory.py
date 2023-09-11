# All this is theoretical of course.
# This is a collection of scripts i found online while learning about graph theory
# Mostly https://python-course.eu/applications-python/graphs-python.php

'''
        a       b
         \     /|
          \   / |
            c   |      f
           / \  |
          /   \ |
        d       e
'''

# graphs in python are represented as sets
# vetice : { edges }
graph = {
    'a': {'c'},
    'b': {'c', 'e'},
    'c': {'a', 'b', 'd', 'e'},
    'd': {'c', 'e'},
    'e': {'b', 'c'},
    'f': {}
}

from typing import TypeVar, Any
from collections import defaultdict

T = TypeVar("T")

# Function to generate a list of all edges in the graph
def generate_edges(graph: set[T]) -> list[T]:
    edges: list[T] = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append({node, neighbor})
    
    return edges

# Calculate numebr of isolated nodes in a given graph
def find_isolated_nodes(graph: set[T]) -> set:
    isolated = set()
    for node in graph:
        if not graph[node]:
            isolated.add(node)
    
    return isolated


print(generate_edges(graph))
print(find_isolated_nodes(graph))


# ================================================================================================

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
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
        res += "\nedges"
        for edge in self.__generate_edges():
            res += str(edge)

        return res