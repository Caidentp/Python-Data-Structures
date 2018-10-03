from abstract_stack import AbstractStack


class DynamicArrayStack(AbstractStack):
    """Dynamic stack, has the ability to expand.
    """

    def __init__(self, size=10):
        super().__init__()
        self.array = [None] * size

    def __iter__(self):
        temp = self.top
        while temp != -1:
            yield self.array[temp]
            temp -= 1

    def push(self, data):
        self.top += 1
        if self.top == len(self.array):
            self.expand_array()
        self.array[self.top] = data

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        data = self.array[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.array[self.top]

    def expand_array(self):
        """Doubles array size once full.
        """

        self.array += [None] * len(self.array)