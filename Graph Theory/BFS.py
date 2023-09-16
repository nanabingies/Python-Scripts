# BFS pseudocode

"""
create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbors of u
"""

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


def BFS(visited: list, graph: dict, startNode: T):
    queue: list = []
    queue.append(startNode)
    visited.append(startNode)
    
    while queue:
        head: T = queue.pop(0)
        print(head, end=' ')

        for neighbor in graph[head]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    visited: list = []
    BFS(visited, graph, '5')