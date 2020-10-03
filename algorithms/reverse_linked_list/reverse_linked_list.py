import datetime
import random

LL_DATA_FILENAME = 'data.txt'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add_to_end(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def load_random_values(self, size):
        counter = 0
        while counter < size:
            counter += 1
            if counter % 100000 == 0:
                print(counter)
            self.add_to_end(random.randint(10, 10000000))

    def read(self, filename):
        """Populates the linked list from a text file.

        :param str filename: The file containing the values.
        """
        counter = 0
        with open(filename, 'r') as file:
            while True:
                line = file.readline()
                counter += 1
                # if counter % 100000 == 0:
                #     print(counter)
                if not line:
                    break
                self.add_to_end(int(line.strip()))

    def reverse(self):
        if not self._head:
            return
        previous = None
        n = self._head
        while n:
            n2 = n.next
            n.next = previous
            previous = n
            n = n2
        self._head, self._tail = self._tail, self._head

    def print(self):
        node = self._head
        while node:
            print(node.value)
            node = node.next


if __name__ == '__main__':
    ll = LinkedList()
    print("Reading")
    t1 = datetime.datetime.now()
    ll.read(LL_DATA_FILENAME)
    t2 = datetime.datetime.now()
    print(f"Reading took: {(t2 - t1).total_seconds()} seconds", )
    print("Reversing")
    t1 = datetime.datetime.now()
    ll.reverse()
    t2 = datetime.datetime.now()
    print(f"Reversing took: {(t2 - t1).total_seconds()} seconds", )
