class Node(object):

    max_size = 10

    def __init__(self):
        self.array = [0] * Node.max_size
        self.top = 0
        self.next = None
        self.previous = None


class Stack(object):

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node()

        elif self.head.top == 10:
            new_node = Node()
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.head.array[self.head.top] = data
        self.head.top += 1

    def pop(self):
        if self.head is not None:
            self.head.top -= 1
            data = self.head.array[self.head.top]

            if self.head.top == 0:
                self.head = self.head.next

                if self.head is not None:
                    self.head.previous = None
            return data

    def peek(self):
        if self.head is not None:
            return self.head.array[self.head.top-1]

    def empty(self):
        return self.head is None
