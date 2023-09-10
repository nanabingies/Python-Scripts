# Hash Table implementation

from typing import Any

class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key: Any):
        h = self.get_hash(key)
        return self.arr[h]
    
if __name__ == "__main__":
    hash = HashTable()
    hash.add('March 6', 130)
    print(hash.get('March 6'))