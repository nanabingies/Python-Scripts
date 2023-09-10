
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

    def __str__(self) -> str:
        strng: str = ""

        if self.head is None:
            return strng
        
        if self.head.next is None:
            return str(self.head.data) + " -> NULL"
        
if __name__ == "__main__":
    double = DoubleList()
    double.insert(1)
    print(double)