#!/usr/bin/python3
"""module for a singly linke list"""


class Node:
    """defines a node"""
    def __init__(self, data, next_node=None):
        """initialzes the node with instance vairbales"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""
        return (self.__data)
    
    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value
    
    @property
    def next_node(self):
        """gets next node"""

        return (self.__next_node)
    
    @next_node.setter
    def next_node(self, value):
        """set value for next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must a Node object')

        self.__next_node = value

class SinglyLinkedList():
    """defines a singly linked list"""
    def __init__(self):
        """initialize the singly linked list"""
        self.head = None
    def __str__(self):
        """make list printable"""

        prints = ""
        location = self.__head

        if location is not None:
            while location is not None:
                prints += str(location.data) + "\n"
                location = location.next_node
        return prints[:-1]
    def sorted_insert(self, value):
        """insert in sorted fashion"""
        node = self.__head
        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
                node.next_node = Node(value, node.next_node)
