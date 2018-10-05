from abstract_queue import *


class Node:
    """Class for creating linked list nodes.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue(AbstractQueue):
    """Class for creating a queue out of a linked list.
    """

    def __init__(self, node=None):
        super().__init__()
        self.head = node
        self.back = node

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def enqueue(self, data):
        """Add an item to the queue.
        """

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size += 1

    def dequeue(self):
        """Remove an item from the queue.
        """

        if self.is_empty():
            raise IndexError('Queue is empty.')
        value = self.head.data
        if self.head == self.back:
            self.head = None
            self.back = None
        else:
            self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        """Return the first element in a queue without removing it.
        """

        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self.head.data
