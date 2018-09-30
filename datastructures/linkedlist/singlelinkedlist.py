from abstract_linked_list import (
	AbstractSingleOrDoubleLinkedList,
	SingleLLNode
)


class SingleLinkedList(AbstractSingleOrDoubleLinkedList):
    """Class for singly linked list.
    """

    def __init__(self, head_node=None):
        super().__init__(head_node)

    def push(self, new_node_data):
        """Add a node to the beginning of a list.

        args:
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = SingleLLNode(new_node_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_node_data):
        """Add a new node to the end of a list.

        args:
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = SingleLLNode(new_node_data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert(self, index, new_node_data):
        """Insert a node into a linked list by position.
        
        args:
            index: position to insert a node at
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = SingleLLNode(new_node_data)
        counter = 0

        if index == 0:
            self.push(new_node_data)
            return

        if (index >= len(self)):
            self.append(new_node_data)
            return

        temp = self.head

        while counter < (index-1):
            temp = temp.next 
            counter += 1

        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, index):
        """Delete a node by position.

        args:
            index: position of node to be deleted
        """

        if not self.head:
            raise ValueError('List is empty')

        if index >= len(self):
            raise IndexError('List index out of range')

        temp = self.head

        if index == 0:
            self.head = temp.next
            return

        for x in range(index-1):
            temp = temp.next

        next_node = temp.next.next
        temp.next = next_node
