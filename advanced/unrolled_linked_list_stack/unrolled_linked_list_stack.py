class Node(object):

    max_size = 10

    def __init__(self, next=None):
        self.array = [0] * Node.max_size
        self.top = 0
        self.next = next


class Stack(object):

    def __init__(self):
        self.head = None
        
    def __getitem__(self, index):
        return self.head.array[index]
    
    def __setitem__(self, index, key):
        self.head.array[index] = key

    def push(self, data):
        if self.head is None:
            self.head = Node()
        elif self.head.top == 10:
            self.head = Node(self.head)

        self[self.head.top] = data
        self.head.top += 1

    def pop(self):
        if self.head is not None:
            self.head.top -= 1
            data = self[self.head.top]

            if self.head.top == 0:
                temp = self.head
                self.head = self.head.next
                temp.next = None
            return data

    def peek(self):
        if self.head is not None:
            return self.head.array[self.head.top-1]

    def empty(self):
        return self.head is None
