"""Detects cycles in a linked list."""


class Node:
    """Node that exposes the has_cycle.

    :ivar _value: The value that the Node holds.
    :ivar Node _next: The next Node of the list.
    """

    def __init__(self, value):
        """Initializer.

        :param value: The value that the Node holds.
        """
        self._value = value
        self._next = None

    def set_next(self, other):
        """Sets the next node.

        :param Node other: The next Node of the list.
        """
        self._next = other

    def get_next(self):
        """Gets the next node.

        :returns: The next node.
        :rtype: Node.
        """
        return self._next

    def add(self, value):
        """Adds a new node to the linked list.

        :param value: The value of the new node to add.
        """
        if not self._next:
            self.set_next(Node(value))
            return self._next
        else:
            return self._next.add(value)

    def has_cycle(self):
        """Checks whether the linked list contains a cycle.

        :return: True if the linked list contains a cycle.
        :rtype: bool
        """
        p1 = self
        p2 = self
        while p1 and p2:
            p1 = p1.get_next()
            if not p1:
                break

            p2 = p2.get_next()
            if not p2:
                break

            p2 = p2.get_next()
            if not p2:
                break

            if p1 is p2:
                return True
        return False
