# Implement the below Tree in python

'''
    Nilupul (CEO)
        |__ Chinmay (CTO)
            |__ Vishwa (Infrastructure Head)
                |__ Dhaval (Cloud Manager)
                |__ Abhijit (App Manager)
            |__ Ahmir (Application Head)
        |__ Ghels (HR Head)
            |__ Peter (Recruitment Manager)
            |__ Waqas (Policy Manager)
'''

from typing import Any, Generic, TypeVar

T = TypeVar('T')

class Trees:
    parent: None
    children: list[T]
    data: T

    def __init__(self, data: T) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def addNode(self, node: T) -> None:
        self.parent = self
        self.children.append(node)

    def printNodes(self):
        print(self.data)
        if self.children:
            for _child in self.children:
                _child.printNodes()

if __name__ == "__main__":
    root = Trees("Nilupul (CEO)")
    root.printNodes()
    print("\n============================\n")

    tech = Trees("Chinmay (CTO)")
    hr = Trees("Ghels (HR Head)")

    root.addNode(tech)
    root.addNode(hr)
    root.printNodes()
    print("\n============================\n")

    infrs = Trees("Vishwa (Infrastructure Head)")
    app = Trees("Ahmir (Application Head)")
    tech.addNode(infrs)
    tech.addNode(app)
    hr.addNode(Trees("Peter (Recruitment Manager)"))
    hr.addNode(Trees("Waqas (Policy Manager)"))
    root.printNodes()
    print("\n============================\n")

    infrs.addNode(Trees("Dhaval (Cloud Manager)"))
    infrs.addNode(Trees("Abhijit (App Manager)"))
    root.printNodes()
