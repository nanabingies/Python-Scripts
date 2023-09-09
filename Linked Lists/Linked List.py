# Linked List implementation in python

class Node:
    item: int

    # Creating a node
    def __init__(self, item: int) -> None:
        self.item = item
        self.next = None

class LinkedList:
    head: Node

    def __init__(self) -> None:
        self.head = None


if __name__ == "__main__":
    linkedlist = LinkedList()

    # Assign item values
    first = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linkedlist.head = first
    linkedlist.head.next = second
    second.next = third

    # Print the linked list items
    while linkedlist.head != None:
        print(linkedlist.head.item, end=" ")
        linkedlist.head = linkedlist.head.next
