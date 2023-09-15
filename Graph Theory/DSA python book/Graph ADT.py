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

    def __init__(self, u, v, x) -> None:
        """ Do not call constructor directly. Use Graph's insert_edge(u,v,x) """
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self) -> tuple:
        """ Return (u,v) tuple for vertices u and v """
        return (self._origin, self._destination)
    
    def opposite(self, v) -> Vertex:
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
        