# The following code is for checking if a tree is a full binary tree.

from dataclasses import dataclass
from typing import TypeVar
T = TypeVar("T")

@dataclass
class Node:
    item: int 
    left: T
    right: T

    def __init__(self, item: int):
        self.item = item
        self.left = None
        self.right = None

# Check if it's a full binary tree
def isFullTree(root: Node) -> bool:
    if root is None:
        return True
    
    # Checking whether child is present
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))
    
    return False

root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

if isFullTree(root):
    print("Full Binary Tree")
else:
    print("I don't even know what tree this is")