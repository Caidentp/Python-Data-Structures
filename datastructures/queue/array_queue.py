from abstract_queue import *


class ArrayQueue(AbstractQueue):
    """Class for creating a queue out of a list.
    """

    _capacity = 10

    def __init__(self):
        super().__init__()
        self.array = [None] * ArrayQueue._capacity
        self.front = 0
        self.back = 0

    def __iter__(self):
        temp = self.front
        while self.array[temp]:
            yield self.array[temp]
            temp += 1

    def enqueue(self, data):
        """Add an item to the queue.
        """
        
        if self.back == len(self.array):
            self.expand()
        self.array[self.back] = data
        self.back += 1
        self.size += 1

    def dequeue(self):
        """Remove an item from the queue.
        """

        if self.is_empty():
            raise IndexError('Queue is empty.')
        item = self.array[self.front]
        self.array[self.front] = None
        self.front += 1
        self.size -= 1
        return item

    def peek(self):
        """Return the first element in a queue without removing it.
        """

        if self.is_empty():
            raise IndexError('Queue is empty.')
        return self.array[self.front]

    def expand(self):
        """Doubles the size of the queue.
        """

        self.array += [None] * len(self.array)

    @classmethod
    def change_capacity(cls, new_capacity):
        """Change the capacity class variable.
        """

        cls.capacity = new_capacity
