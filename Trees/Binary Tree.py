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
    
    def traverse_preorder(self) -> list[int]:
        # For preorder traversal we first visit the root node, then the left tree node, then right tree node
        elements: list[int] = []

        if self.root:
            elements.append(self.root)

        if self.left:
            elements += self.left.traverse_preorder()

        if self.right:
            elements += self.right.traverse_preorder()

        return elements
    
    def traverse_postorder(self) -> list[int]:
        # For postorder traversal we first visit the left tree node, then right tree node, and finally the root node
        elements: list[int] = []

        if self.left:
            elements += self.left.traverse_postorder()
        if self.right:
            elements += self.right.traverse_postorder()
        elements.append(self.root)

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
            
    def delete(self, value: int):
        if value < self.root:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.root:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.root = min_val
            self.right = self.right.delete(min_val)

        return self
            
    # The following methods are exercises implemented by ME
    def find_min(self) -> int:
        if self.root is None:
            return
        
        if self.left is None:
            return self.root
        
        if self.left:
            return self.left.find_min()
        
    def find_max(self) -> int:
        if self.root is None:
            return
        
        if self.right is None:
            return self.root
        
        if self.right:
            return self.right.find_max()
        
    

def buildTree(elements: list[int]) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    elements: list = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    root: BinarySearchTreeNode = buildTree(elements)
    print(root.traverse_inorder())
    print(root.traverse_preorder())
    print(root.traverse_postorder())
    print(root.search(27))

    print(root.find_min())
    print(root.find_max())

    root.delete(20)
    print(root.traverse_inorder())
