
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_as_str(self):
        tokens = [self.value]
        if self.next:
            tokens += self.next.get_as_str()
        return tokens

    def add(self, value):
        if not self.next:
            self.next.add(value)
        else:
            self.next = Node(value)

    def reverse(self, previous):
        nn = self.next
        self.next = previous
        if not self.next:
            return self
        if nn:
            return nn.reverse(self)


class LinkedList:
    _root = None

    def add(self, value):
        if not self._root:
            self._root = Node(value)
        else:
            self._root.add(Node(value))

    def reverse(self):
        if self._root:
            self._root = self._root.reverse(previous=None)

    def __str__(self):
        if self._root:
            return ','.join(self._root.get_as_str())
        return 'empty'


ll = LinkedList()
for i in range(1, 10):
    ll.add(i)
print(ll)
ll.reverse()
print(ll)

