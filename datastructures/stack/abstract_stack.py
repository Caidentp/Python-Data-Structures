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
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass
