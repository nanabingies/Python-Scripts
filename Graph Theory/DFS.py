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


def DFS(visited: set, graph:dict, startNode: T):
    for startNode in graph:
        if startNode not in visited:
            print(startNode)
            visited.add(startNode)
            for neighbor in graph[startNode]:
                DFS(visited, graph, neighbor)

if __name__ == "__main__":
    visited = set()
    DFS(visited, graph, '5')