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

class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initialize the singly linked list"""
        self.head = None
    def __str__(self):
        """make list printable"""

        prints = ""
        location = self.head
        while location:
            prints += str(location.data) + "\n"
            location = location.next_node
        return prints[:-1]
    def sorted_insert(self, value):
        """insert in sorted fashion"""
        
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_nodee = location.next_node
        location.next_node = new
