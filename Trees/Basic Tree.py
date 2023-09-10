# Basic Tree implementation

from typing import Any 

class TreeNode:
    data: Any
    children: list 
    parent: Any

    def __init__(self, data: Any) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child: Any) -> None:
        child.parent = self
        self.children.append(child)

def build_product_tree() -> TreeNode:
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    print(root)
