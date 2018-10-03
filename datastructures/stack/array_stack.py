from abstract_stack import AbstractStack


class ArrayStack(AbstractStack):
    """Fixed-size stack, cannot expand once it is full.
    """

    max_size = 5

    def __init__(self):
        super().__init__()
        self.array = [None] * ArrayStack.max_size

    def __iter__(self):
        temp = self.top
        while temp != -1:
            yield self.array[temp]
            temp -= 1

    def is_full(self):
        return len(self) == ArrayStack.max_size

    def push(self, data):
        if self.is_full():
            raise IndexError("Stack is full.")
        self.top += 1
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

    @classmethod
    def change_max_size(cls, new_max_size):
        cls.max_size = new_max_size