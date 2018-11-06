from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):
    """Defines methods common to different types of linked lists.
    """

    def __init__(self, head_node):
        self.head = head_node
        self.tail = head_node
        if head_node is None:
            self.size = 0
        else:
            self.size = 1
        
    def __len__(self):
        """Make instances of linked lists work with Python's len() 
           function.

        returns: how many nodes are present in the linked list
        """

        return self.size

    def __getitem__(self, index):
        """Operator overloading [] for retrieving the index of a linked 
           list.

        args:
            index: position of linked list node to find

        returns: data instance variable of appropriate node
        """

        if index > len(self) or self.head is None:
            raise IndexError('List index out of range')

        temp = self.head

        for x in range(index):
            temp = temp.next
        return temp.data
        
    def __iter__(self):
        """Makes instances of linked lists work with keywords that use 
           the iterator protocol.
        """

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
    def insert(self, index, new_node_data):
        """Insert a node into a linked list by position.
        
        args:
            index: position to insert a node at
            new_node_data: this will become the data instance variable 
                           of a node class
        """
        pass

    @abstractmethod
    def delete(self, index):
        """Delete a node by position.

        args:
            index: position of node to be deleted
        """

        pass


class AbstractNode(object):
    """Defines methods common to all types of linked list nodes.
    """

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
    """Singly linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)


class DNode(AbstractNode):
    """Doubly linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)
        self.previous = None


class CNode(AbstractNode):
    """Circular linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)
        self.next = self
