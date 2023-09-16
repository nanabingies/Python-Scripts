# Using a Python dictionary to act as an adjacency list

from typing import TypeVar
T = TypeVar("T")

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


def DFS(visited: set, graph:dict, node: T):
    for node in graph:
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                DFS(visited, graph, neighbor)

if __name__ == "__main__":
    visited = set()
    DFS(visited, graph, '5')