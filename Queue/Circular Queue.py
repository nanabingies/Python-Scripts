# Circular Queue implementation in Python

class CircularQueue:
    num: int
    head: int
    tail:int
    queue: list

    def __init__(self, num: int) -> None:
        self.num = num
        self.queue = [None] * num
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data: int) -> None:
        if ((self.tail + 1) % self.num == self.head):
            print("The citcular queue is full")
            return
        
        if self.head == -1:
            self.head = 0
            self.tail=0
            self.queue[self.tail] = data

        else:
            self.tail = (self.tail + 1) % self.num      # is the % self.num really needed ??
            self.queue[self.tail] = data

        return
    
    # Delete an element from the circular queue
    def dequeue(self) -> int:
        if self.head == -1:
            print("The circular queue is empty")
            return None
        
        if self.head == self.tail:
            # Only one item in queue, delete it
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.num
            return temp
        
    def printCQueue(self):
        if self.head == -1:
            print("No element in the circular queue")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail):
                print(self.queue[i], end=" ")
            print()

        else:
            for i in range(self.head, self.num):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

if __name__ == "__main__":
    circ = CircularQueue(5)
    circ.enqueue(1)
    circ.enqueue(2)
    circ.enqueue(3)
    circ.enqueue(4)
    print(f"Initial queue {circ.printCQueue()}")

    circ.dequeue()
    circ.printCQueue()
