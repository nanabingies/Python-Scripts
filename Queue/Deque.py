# Dequeue implementation in python

class Deque:
    items: list

    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []
    
    def addRear(self, item: int) -> None:
        self.items.append(item)

    def addFront(self, item: int) -> None:
        self.items.insert(0, item)

    def removeFront(self) -> int:
        return self.items.pop(0)
    
    def removeRear(self) -> int:
        return self.items.pop()
    
    def size(self) -> int:
        return len(self.items)
    
    
if __name__ == "__main__":
    d = Deque()
    print(d.isEmpty())
    d.addRear(8)
    d.addRear(5)
    d.addFront(7)
    d.addFront(10)
    print(d.size())
    print(d.isEmpty())
    print(d.items)
    
    d.addRear(11)
    print(d.removeRear())
    print(d.removeFront())

    d.addFront(55)
    d.addRear(45)
    print(d.items)