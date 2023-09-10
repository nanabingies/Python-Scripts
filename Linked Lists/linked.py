
# My linked list implementation

from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: None

class List:
    head: Node

    def __init__(self) -> None:
        self.head = None
        pass

    def insert(self, data: int) -> None:
        node = Node(data, None)

        if self.head is None:       # Empty list
            self.head = node
            return
        
        if self.head.next is None:  # Only one element in list
            self.head.next = node
            return
        
        # There are more elements in the list.
        # Move to end and append
        _last: Node = self.head
        while _last.next is not None:
            _last = _last.next
        _last.next = node
        return
    
    def insertFront(self, data: int) -> None:
        node: Node = Node(data, None)
        
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
    
    def remove(self, data: int) -> bool:
        if self.head is None:
            print('Cant find node with value ', data, ' in the list')
            return False
        
        if self.head.next is None:
            if self.head.data == data:
                self.head = None
                return True
        
        _temp: Node = self.head
        while _temp.next is not None:
            if _temp.next.data == data:
                _prev = _temp
                _next = _temp.next.next
                
                if _next is not None:
                    _prev.next = _next
                else:
                    _prev.next = None
                return True

            _temp = _temp.next


    def find(self, data: int) -> Node:
        if self.head is None:
            return None
        
        _temp: Node = self.head
        foundNode: Node = None

        while _temp is not None:
            if _temp.data == data:
                foundNode = _temp
                break

            _temp = _temp.next

        return foundNode
        
    def __str__(self) -> str:
        strng: str = ""

        if self.head is None:
            return strng
        
        _temp = self.head
        while _temp is not None:        # Look for way to concatenate the strings
            print(_temp.data, end=" -> ")
            _temp = _temp.next
        print("NULL")

        return strng

    
if __name__ == "__main__":
    linkd = List()
    
    linkd.insert(1)
    linkd.remove(1)
    print(linkd)
    linkd.insert(2)
    linkd.insertFront(1)
    linkd.insert(10)
    linkd.insert(15)
    linkd.insert(4)
    linkd.insert(23)
    linkd.insert(18)

    print(linkd)

    _auto = linkd.find(23)
    if _auto is not None:
        print(f'Found {_auto.data} is list')
    print(linkd)

    linkd.remove(23)
    print(linkd)
    linkd.remove(18)
    print(linkd)
    linkd.remove(10)
    print(linkd)
    linkd.remove(15)
    print(linkd)
    
    