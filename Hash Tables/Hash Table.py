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
    
    def __setitem__(self, key: Any, val: int) -> None:
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key: Any) -> int:
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key: Any) -> None:
        h = self.get_hash(key)
        self.arr[h] = None
    
if __name__ == "__main__":
    hash = HashTable()
    hash['March 6'] = 130
    print(hash['March 6'])

    hash['March 1'] = 20
    hash['December 27'] = 27
    del hash['March 1']
    print(hash['March 1'])