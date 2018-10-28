from abstract_linked_list import (
    AbstractLinkedList,
    CircleLLNode
)


class CircularLinkedList(AbstractLinkedList):
    """Class for circular linked list.
    """

    def __init__(self, head_node=None):
        super().__init__(head_node)

    def push(self, new_node_data):
        """Add a node to the beginning of a list.

        args:
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = CircleLLNode(new_node_data)

        if not self.head:
            self.head = new_node
            return
        temp = self.head
        new_node.next = temp
        condition = True

        while condition:
            temp = temp.next
            if temp.next is self.head:
                condition = False
        temp.next = new_node
        self.head = new_node

    def append(self, new_node_data):
        """Add a new node to the end of a list.

        args:
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = CircleLLNode(new_node_data)

        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head    
        temp = self.head
        condition = True

        while condition:
            temp = temp.next
            if temp.next is self.head:
                condition = False
        temp.next = new_node

    def insert(self, index, new_node_data):
        """Insert a node into a linked list by position.

        args:
            index: position to insert a node at
            new_node_data: this will become the data instance variable of a node class
        """

        new_node = CircleLLNode(new_node_data)

        if index == 0:
            self.push(new_node_data)
            return

        if (index > len(self)):
            self.append(new_node_data)
            return
        temp = self.head
        counter = 0

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

        if not self.head or index >= len(self):
            raise IndexError('List index out of range')
        temp = self.head

        if index == 0:
            condition = True

            while condition:
                temp = temp.next
                if temp.next is self.head:
                    condition = False
            temp.next = self.head.next
            self.head = self.head.next
            return

        for x in range(index-1):
            temp = temp.next
            if temp.next is self.head:
                break
        next_node = temp.next.next
        temp.next = next_node
