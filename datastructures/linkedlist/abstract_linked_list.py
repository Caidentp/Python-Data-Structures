from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):
    """Defines methods common to different types of linked lists.
    """

    def __init__(self, head_node):
        self.head = head_node

    def __getitem__(self, index):
        """Operator overloading [] for retrieving the index of a linked list.

        args:
            index: position of linked list node to find

        returns: data instance variable of appropriate node
        """
        
        counter = 0
        temp = self.head

        if index > len(self) or not self.head:
            raise IndexError('List index out of range')

        while counter < index:
            temp = temp.next
            counter += 1

        return temp.data

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
    def __len__(self):
        pass

    @abstractmethod
    def push(self, new_node_data):
        pass

    @abstractmethod
    def append(self, new_node_data):
        pass

    @abstractmethod
    def insert(self, index, new_node_data):
        pass

    @abstractmethod
    def delete_node(self, index):
        pass
	

class AbstractSingleOrDoubleLinkedList(AbstractLinkedList):
    """Defines methods common to both singly and doubly linked lists.
    """

    def __init__(self, head_node):
        super().__init__(head_node)

    def __len__(self):
        """Make instances of linked lists work with Python's len() function.

        returns: how many nodes are present in the linked list
        """

        counter = 0
        temp = self.head

        while temp:
            counter += 1
            temp = temp.next

        return counter

    def __iter__(self):
        """Makes instances of linked lists work with keywords that use the iterator protocol.
        """

        temp = self.head

        while temp:
            yield temp.data
            temp = temp.next


class AbstractNode(object):
    """Defines methods common to all types of linked list nodes.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        template = "{}({}) object at <{}>"
        return template.format(self.__class__.__name__, self.__dict__, id(self))

    def __repr__(self):
        return "Node(data={0})".format(self.data)


class SingleLLNode(AbstractNode):
    """Singly linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)


class DoubleLLNode(AbstractNode):
    """Doubly linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)
        self.previous = None


class CircleLLNode(AbstractNode):
    """Circular linked list node.
    """

    def __init__(self, data=None):
        super().__init__(data)
        self.next = self
