
# My implementation of the double linked list data structure

from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: None
    prev: None

class DoubleList:
    head: Node

    def __init__(self) -> None:
        self.head = None

    def insert(self, data: int) -> None:
        node: Node = Node(data, None, None)

        if self.head is None:
            self.head = node
            return
        
        if self.head.next is None:
            self.head.next = node
            node.prev = self.head
            return
        
        # Handle multiple cases
        _last: Node = self.head
        while _last.next is not None:
            _last = _last.next
        
        # we're now at last
        _last.next = node
        node.prev = _last
        return
    
    def deleteFirst(self) -> None:
        if self.head is None:
            return
        
        # Only one item in list ???
        if self.head.next is None:
            self.head = None
            return
        
        _temp: Node = self.head
    
    def deleteNum(self, data: int) -> None:
        _temp: Node

        if self.head is None:
            return
        
        if self.head.next is None:
            if self.head.data == data:
                self.head = None
                return

    def __str__(self) -> str:
        strng: str = ""

        if self.head is None:
            return strng
        
        if self.head.next is None:
            strng += (str(self.head.data) + " -> NULL")
            return strng
        
        _temp: Node = self.head
        while _temp is not None:
            strng += (str(_temp.data) + " -> ")
            _temp = _temp.next 

        strng += "NULL"
        return strng

        
if __name__ == "__main__":
    double = DoubleList()
    double.insert(1)
    double.insert(4)
    double.insert(8)
    double.insert(7)
    print(double)

    double.deleteFirst()
    print(double)