class Stack(object):

    class Node(object):
        max_size = 10
        def __init__(self, next=None):
            self.array = [0] * Stack.Node.max_size
            self.top = 0
            self.next = next

    def __init__(self):
        self.head = None
        self.len = 0

    def __getitem__(self, index):
        return self.head.array[index]

    def __setitem__(self, index, key):
        self.head.array[index] = key

    def __len__(self):
        return self.len

    def push(self, data):
        if self.head is None or self.head.top == 10:
            self.head = Stack.Node(self.head)
        self[self.head.top] = data
        self.head.top += 1
        self.len += 1

    def pop(self):
        if self.head is not None:
            self.head.top -= 1
            data = self[self.head.top]
            if self.head.top == 0:
                temp = self.head
                self.head = self.head.next
                temp.next = None
            self.len -= 1
            return data
        raise IndexError('Empty stack.')

    def peek(self):
        if self.head is not None:
            return self.head.array[self.head.top-1]
        raise IndexError('Empty stack.')

    def empty(self):
        return self.head is None
