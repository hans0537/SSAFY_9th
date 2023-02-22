class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

A = Node("A")
B = Node("B")
C = Node("C")
root = A
A.left = B
A.right = C