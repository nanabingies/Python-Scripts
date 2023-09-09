from queue import PriorityQueue

q = PriorityQueue()
q.put(4)
q.put(8)
q.put(1)
q.put(10)
q.put(3)
print(f"Priority Queue : {q}")

while not q.empty():
    print(f'{q.get()}')