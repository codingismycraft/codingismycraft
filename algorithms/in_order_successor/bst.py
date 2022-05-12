"""Simple Binary search tree supporting in order successor."""


class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    def add_value(self, value):
        if value <= self.__value:
            if not self.__left:
                self.__left = Node(value)
            else:
                self.__left.add_value(value)
        else:
            if not self.__right:
                self.__right = Node(value)
            else:
                self.__right.add_value(value)

    @property
    def left_value(self):
        return self.__left.__value if self.__left else None

    @property
    def right_value(self):
        return self.__right.__value if self.__right else None

    def leftmostvalue(self):
        if self.__left is None:
            return self.__value
        else:
            return self.__left.leftmostvalue()

    def in_order_successor(self, value, last_left=None):
        if value == self.__value:
            if self.__right is None:
                return last_left
            else:
                return self.__right.leftmostvalue()
        elif self.__value >= value:
            if self.__left:
                return self.__left.in_order_successor(
                    value, last_left=self.__value
                )
            else:
                return None
        else:
            if self.__right:
                return self.__right.in_order_successor(
                    value, last_left=last_left
                )
            else:
                return None
