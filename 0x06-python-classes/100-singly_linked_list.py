#!/usr/bin/python3

class Node:
    """
    This is the Node class documentation.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """
        Retrieves the value of the data attribute.
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        """
        Sets the value of the data attribute.

        Args:
            value: The new data value.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """
        Retrieves the value of the next_node attribute.
        """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of the next_node attribute.

        Args:
            value: The new next_node value.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class documentation.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.head = None
    
    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def __str__(self):
        """
        Generates a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
