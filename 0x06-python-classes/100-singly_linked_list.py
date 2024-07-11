#!/usr/bin/python3
"""a class Node that defines a node of a singly linked list
    and a class SinglyLinkedList that defines a singly linked list"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """initializing data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next node setter"""
        if value is not None or not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        """initializing data"""
        self.head = None

    def sorted_insert(self, value):
        """method inserts a new node into the correct position"""
        new_node = Node(value)
        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node

    def list_print(self):
        """print the list one node by line"""
        current = self.__head
        while current:
            print(current.data)
            current = current.next_node
