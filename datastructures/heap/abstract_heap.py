from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __repr__(self):
        template = "{}({})"
        return template.format(self.__class__.__name__, self.__dict__)

    def __str__(self):
        template = "<{} object at {}>"
        mem_address = '0x' + '{:0>16}'.format(hex(id(self)).upper()[2:])
        return template.format(self.__class__.__name__, mem_address)

    def __add__(self, other):
        new_heap = Heap()
        for item in self.heap:
            new_heap.insert(item)
        for item in other.heap:
            new_heap.insert(item)
        return new_heap

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.heap[index]

    def __setitem__(self, index, key):
        self.heap[index] = key

    def delete_top(self):
        """Delete root node in a heap tree and return its value."""
        minimum = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._perc_down(1)
        return minimum

    def insert(self, data):
        """Insert a node into the heap in the appropriate position.

        args:
            data: value of node to insert into heap.
        """
        self.heap.append(data)
        self.size += 1
        self._perc_up(self.size)

    @classmethod
    def from_iterable(cls, iterable):
        """Create a heap object from an iterable object and return it.

        args:
            iterable: any iterable object to turn into a heap.
        """
        new_heap = cls()
        new_heap.size = len(iterable)
        new_heap.heap += list(iterable)
        x = len(iterable) // 2
        while x > 0:
            new_heap._perc_down(x)
            x -= 1
        return new_heap

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def _perc_up(self, index):
        """Compares node to its parent and swaps the values if needed.

        args:
            index: index of node to compare to its parent.
        """
        pass

    @abstractmethod
    def _perc_down(self, index):
        """Compares a node to its children and swaps the values if needed.

        args:
            index: index of node to compare to its children.
        """
        pass

    @abstractmethod
    def successor_child_index(self, index):
        """Finds the most feasible successor child for swapping values with its parent if needed.

        args:
            index: index of parent to compare to its children.
        """
        pass