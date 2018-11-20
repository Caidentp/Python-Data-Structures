from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):
    """Defines methods common to different types of linked lists."""
    def __init__(self, head_node):
        self.head = head_node
        self.tail = head_node
        if head_node is None:
            self.size = 0
        else:
            self.size = 1
        
    def __len__(self):
        return self.size

    def __getitem__(self, index: 'int'):
        if self.head is not None and index < len(self):
            if index < 0:
                if abs(index) > len(self):
                    raise IndexError('List index out of range.')
                index = len(self) + index
            probe = self.head

            for x in range(index):
                probe = probe.next
            return probe.data
        raise IndexError('List index out of range.')

    def __setitem__(self, index: 'int', data):
        if self.head is not None and index < len(self):
            if index < 0:
                if abs(index) > len(self):
                    raise IndexError('List index out of range.')
                index = len(self) + index

            probe = self.head
            for x in range(index):
                probe = probe.next
            probe.data = data
        else:
            raise IndexError('List index out of range.')

    def __iter__(self):
        if self.head is not None:
            temp = self.head
            condition = True
            while condition:
                yield temp.data
                temp = temp.next
                if temp is self.head or temp is None:
                    condition = False

    def __str__(self):
        template = "{}({})"
        return template.format(self.__class__.__name__, self.__dict__)

    def __repr__(self):
        template = "<{} object at {}>"
        mem_address = '0x' + '{:0>16}'.format(hex(id(self)).upper()[2:])
        return template.format(self.__class__.__name__, mem_address)

    @abstractmethod
    def push(self, new_node_data):
        """Add a node to the beginning of a list.

        args:
            new_node_data: this will become the data instance variable 
                of a node class
        """
        pass

    @abstractmethod
    def append(self, new_node_data):
        """Add a new node to the end of a list.

        args:
            new_node_data: this will become the data instance variable 
                of a node class
        """
        pass

    @abstractmethod
    def insert(self, index: 'int', new_node_data):
        """Insert a node into a linked list by position.

        args:
            index: position to insert a node at
            new_node_data: this will become the data instance variable 
                of a node class
        """
        pass

    @abstractmethod
    def delete(self, index: 'int'):
        """Delete a node by position.

        args:
            index: position of node to be deleted
        """
        pass


class AbstractNode(object):
    """Defines methods common to all types of linked list nodes."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        template = "{}({}) object at <{}>"
        return template.format(self.__class__.__name__,
                               self.__dict__, id(self))

    def __repr__(self):
        return "Node(data={0})".format(self.data)


class SNode(AbstractNode):
    """Singly linked list node."""
    def __init__(self, data=None):
        super().__init__(data)


class DNode(AbstractNode):
    """Doubly linked list node."""
    def __init__(self, data=None):
        super().__init__(data)
        self.previous = None


class CNode(AbstractNode):
    """Circular linked list node."""
    def __init__(self, data=None):
        super().__init__(data)
        self.next = self
