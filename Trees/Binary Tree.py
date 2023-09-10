# Binary Search Tree Implementation

class BinarySearchTreeNode:
    root: int       # root node
    left: None      # left node
    right: None     # right node

    def __init__(self, data: int) -> None:
        self.root = data
        self.left = None
        self.right = None

    def add_child(self, data: int) -> None:
        if self.root == data:   # Duplicates aren't allowed
            return
        
        if data < self.root:
            # Add data in left tree node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # Add data in right tree node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def traverse_inorder(self) -> list[int]:
        # For inorder traversal we first visit left tree node, then parent node, then right tree node
        elements: list[int] = []
        
        if self.left:
            elements += self.left.traverse_inorder()
        
        elements.append(self.root)

        if self.right:
            elements += self.right.traverse_inorder()

        return elements
    
    def search(self, value: int) -> bool:
        if self.root == value:
            return True
        
        if value < self.root:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    # The following methods are exercises implemented by ME
    def find_min(self) -> int:
        if self.root is None:
            return
        
        if self.left is None and self.right is None:
            return self.root
        
        if self.left is None and self.right:
            return self.root
        
        if self.left:
            return self.left.find_min()
    

def buildTree(elements: list[int]) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    elements: list = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    root: BinarySearchTreeNode = buildTree(elements)
    print(root.traverse_inorder())
    print(root.search(27))

    print(root.find_min())
