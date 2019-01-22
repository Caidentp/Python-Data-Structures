import os
import sys
import unittest

sys.path.append(os.path.split(os.getcwd())[0])

from doubly_linked_list import *


# Converts a linked list to a list for testing
def convert(linked_list):
    return [x for x in linked_list]


class TestDoublyLinkedList(unittest.TestCase):
    def test_doubly_push_empty_list(self):
        linked_list = DoublyLinkedList()
        linked_list.push(0)
        self.assertEqual([0], convert(linked_list))

    def test_doubly_push_populated_list(self):
        linked_list = DoublyLinkedList(DNode(2))
        linked_list.head.next = DNode(3)
        linked_list.push(1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_doubly_append_empty_list(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        self.assertEqual([1], convert(linked_list))

    def test_doubly_append_populated_list(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(2)
        self.assertEqual([1, 2], convert(linked_list))

    def test_doubly_insert_empty_list(self):
        linked_list = DoublyLinkedList()
        with self.assertRaises(IndexError):
            linked_list.insert(0, 1)

    def test_doubly_insert_populated_list(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(3)
        linked_list.append(4)
        self.assertEqual([1, 3, 4], convert(linked_list))
        linked_list.insert(1, 2)
        self.assertEqual([1, 2, 3, 4], convert(linked_list))

    def test_doubly_insert_at_head(self):
        linked_list = DoublyLinkedList(DNode(2))
        linked_list.append(3)
        self.assertEqual([2, 3], convert(linked_list))
        linked_list.insert(0, 1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_doubly_insert_out_of_range(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(2)
        with self.assertRaises(IndexError):
            linked_list.insert(9, 3)

    def test_doubly_delete_node_at_head(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete(0)
        self.assertEqual([2, 3], convert(linked_list))

    def test_doubly_delete_node_at_tail(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete(2)
        self.assertEqual([1, 2], convert(linked_list))
        with self.assertRaises(IndexError):
            linked_list.delete(10)

    def test_doubly_delete_node_in_middle(self):
        linked_list = DoublyLinkedList(DNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete(1)
        self.assertEqual([1, 3], convert(linked_list))


if __name__ == '__main__':
    unittest.main()