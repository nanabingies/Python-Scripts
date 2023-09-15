# Data Structures and ALgorithms in Python

from typing import TypeVar
T = TypeVar("T")

#------------------------- nested Vertex class -------------------------
class Vertex:
    """ Lightweight vertext structure for a graph """
    __slots__ = '_element'

    def __init__(self, x) -> None:
        """ Do not call constructor directly. Use Graph's insert vertex(x). """
        self._element = x

    def element(self) -> T:
        """ Returns element associated with this vertex """
        return self._element
    
    def __hash__(self) -> int:
        """" will allow vetres to be a map/set key """
        return hash(id(self))
    
#------------------------- nested Edge class -------------------------
class Edge:
    """ Lightweight edge structure for a graph """
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u: T, v: T, x: Vertex) -> None:
        """ Do not call constructor directly. Use Graph's insert_edge(u,v,x) """
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self) -> tuple:
        """ Return (u,v) tuple for vertices u and v """
        return (self._origin, self._destination)
    
    def opposite(self, v: T) -> Vertex:
        """ Returns the vertex that is opposite v on this edge """
        return self._destination if v is self._origin else self._origin
    
    def element(self) -> Vertex:
        """ Return element associated with this edge """
        return self._element
    
    def __hash__(self) -> int:
        return hash((self._origin, self._destination))
    

class Graph:
    """ Representation of a simple graph using an adjacency map """

    def __init__(self, directed: bool = False) -> None:
        """ Create an empty graph (undirected, by default) """
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """ Return True if this is a directed graph """
        return self._incoming is not self._outgoing     # directed if maps are distinct
    
    def vertex_count(self) -> int:
        """ Return the number of vertices in the graph """
        return len(self._outgoing)
    
    def vertices(self) -> iter:
        """ Return an iteration of all vertices of the graph """
        return self._outgoing.keys()
    
    def edge_count(self) -> int:
        """ Return the number of edges in the graph """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2
    
    def edges(self) -> set:
        """ Return a set of all edges of the graph """
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self, u: T, v: T) -> T:
        """ Return the edge from u to v, or None if not adjacent """
        return self._outgoing[u].get(v)