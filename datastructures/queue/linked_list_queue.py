from abstract_queue import *


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue(AbstractQueue):

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
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size += 1

    def dequeue(self):
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
        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self.head.data
