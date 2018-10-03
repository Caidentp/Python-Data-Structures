from abstract_stack import AbstractStack


class Node(object):
    """Linked list node to use in stack.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack(AbstractStack):
    """Class for linked list stack.
    """

    def __init__(self, head=None):
        super().__init__()
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        data = self.head.data
        self.head = self.head.next
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.head