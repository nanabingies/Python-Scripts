# Code from Python Data Structures & Algotithm course: Graph Introduction
from typing import TypeVar
T = TypeVar("T")

class Graph:
    _graph_dict: dict
    edges: list

    def __init__(self, edges: list) -> None:
        self.edges = edges
        self._graph_dict = {}

        for start, end in edges:
            if start in self._graph_dict:
                self._graph_dict[start].append(end)
            else:
                self._graph_dict[start] = [end]
        
        print(self._graph_dict)

    def get_paths(self, start: T, end: T, path: list = []) -> list:
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self._graph_dict:
            return []
        
        all_paths: list = []

        for node in self._graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    all_paths.append(p)
        
        return all_paths
    
    def get_shortest_path(self, start: T, end: T, path: list = []) -> list:
        path = path + [start]

        if start == end:
            return path
        
        if start not in self._graph_dict:
            return None
        
        shortest_path = None
        for node in self._graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris",  "Dubai"),
        ("Paris",  "New York"),
        ("Dubai",  "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(f'Paths between {start} and {end} are {route_graph.get_paths(start, end)}')