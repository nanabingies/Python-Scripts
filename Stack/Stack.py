# Stack implementation

class Stack:
    stack: list
    topOfStack: int

    def __init__(self) -> None:
        self.stack = []
        self.topOfStack = -1
        return

    def push(self, num: int) -> None:
        self.stack.append(num)
        self.topOfStack += 1

    def init(self, num: int = 5) -> None:
        for iter in range(num):
            _ = int(input())
            self.stack.append(_)
            self.topOfStack += 1
        print(f'Stack : {self.stack}')

    @property
    def empty(self) -> bool:
        return self.topOfStack == -1
    
    def pop(self) -> int:
        if self.empty == True:
            return None
        
        _ = self.stack.pop()
        return _
    
if __name__ == "__main__":
    stack = Stack()
    print(f'Is stack empty? {stack.empty}')
    stack.init(5)
    print(f'Is stack empty? {stack.empty}')

