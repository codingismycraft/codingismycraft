"""Detects cycles in a linked list."""

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def add(self, value):
        if not self._next:
            self._next = Node(value)
            return self._next
        else:
            return self._next.add(value)

    def __repr__(self):
        if not self._next:
            return f'{self._value}'
        else:
            return f'{self._value} - {self._next.__repr__()}'


root = Node('a')
n1 = root.add("b")
n2 = root.add("c")

print(root)






