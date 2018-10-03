from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    """Defines methods common to different types of stacks.
    """

    def __init__(self):
        self.top = -1

    def __len__(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass