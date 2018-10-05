from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):

    def __init__(self):
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        template = "{}({})"
        return template.format(self.__class__.__name__, self.__dict__)

    def __repr__(self):
        template = "<{} object at {}>"
        mem_address = '0x' + '{:0>16}'.format(hex(id(self)).upper()[2:])
        return template.format(self.__class__.__name__, mem_address)

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def enqueue(self, data):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass
