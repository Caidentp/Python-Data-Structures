from abstract_linked_list import DNode, AbstractLinkedList


class DoublyLinkedList(AbstractLinkedList):
    """Class for doubly linked list.
    """

    def __init__(self, head_node=None):
        super().__init__(head_node)

    def push(self, new_node_data):
        new_node = DNode(new_node_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def append(self, new_node_data):
        new_node = DNode(new_node_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, index, new_node_data):
        if index >= len(self) or self.head is None:
            raise IndexError('List index out of range')
        if index == 0:
            self.push(new_node_data)
        else:
            new_node = DNode(new_node_data)
            temp = self.head
            for x in range(index-1):
                temp = temp.next

            new_node.next = temp.next
            new_node.previous = temp
            new_node.next.previous = new_node
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
                self.head.previous = None
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
            else:
                temp.next.previous = previous
        self.size -= 1
