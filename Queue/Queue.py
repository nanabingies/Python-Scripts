# Queue implementation in Python

class Queue:
    queue: list

    def __init__(self) -> None:
        self.queue = []

    # Add an element
    def enqueue(self, item: int) -> None:
        self.queue.append(item)

    # Remove an element
    def dequeue(self) -> int:
        if len(self.queue) < 1:
            return None
        
        return self.queue.pop(0)
    
    # Display the queue
    def display(self) -> None:
        print(f'Queue : {self.queue}')

    def size(self) -> int:
        return len(self.queue)
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.display()
    queue.dequeue()
    queue.display()