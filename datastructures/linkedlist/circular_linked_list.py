from abstract_linked_list import CNode, AbstractLinkedList


class CircularLinkedList(AbstractLinkedList):
    """Class for circular linked list.
    """

    def __init__(self, head_node=None):
        super().__init__(head_node)

    def push(self, new_node_data):
        new_node = CNode(new_node_data)
        if self.head is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, new_node_data):
        new_node = CNode(new_node_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, new_node_data):
        if index >= len(self) or self.head is None:
            raise IndexError('List index out of range.')
        if index == 0:
            self.push(new_node_data)
        else:
            new_node = CNode(new_node_data)
            temp = self.head
            for x in range(index-1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node
            self.size += 1

    def delete(self, index):
        if index >= len(self) or self.head is None:
            raise IndexError('List index out of range.')
        if index == 0:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            temp = self.head
            previous = self.head
            for x in range(index):
                if temp is self.tail:
                    break
                previous = temp
                temp = temp.next

            previous.next = temp.next
            if temp is self.tail:
                self.tail = previous
                self.tail.next = self.head
        self.size -= 1
