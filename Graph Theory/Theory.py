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
graph = {
    'a': {'c'},
    'b': {'c', 'e'},
    'c': {'a', 'b', 'd', 'e'},
    'd': {'c', 'e'},
    'e': {'b', 'c'},
    'f': {}
}

from typing import TypeVar
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