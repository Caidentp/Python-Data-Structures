from abstract_linked_list import *
from singlelinkedlist import *
from doublelinkedlist import *
from circularlinkedlist import *


import unittest


# Converts a linked list to a list for testing
def convert(linked_list):
    return [x for x in linked_list]


class TestSinglyLinkedList(unittest.TestCase):

    def test_singly_push_empty_list(self):
        linked_list = SingleLinkedList()
        linked_list.push(0)
        self.assertEqual([0], convert(linked_list))

    def test_singly_push_populated_list(self):
        linked_list = SingleLinkedList(SingleLLNode(2))
        linked_list.head.next = SingleLLNode(3)
        linked_list.push(1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_singly_append_empty_list(self):
        linked_list = SingleLinkedList()
        linked_list.append(1)
        self.assertEqual([1], convert(linked_list))

    def test_singly_append_populated_list(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(2)
        self.assertEqual([1, 2], convert(linked_list))

    def test_singly_insert_empty_list(self):
        linked_list = SingleLinkedList()
        linked_list.insert(0, 1)
        self.assertEqual([1], convert(linked_list))

    def test_singly_insert_populated_list(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(3)
        linked_list.append(4)
        self.assertEqual([1, 3, 4], convert(linked_list))
        linked_list.insert(1, 2)
        self.assertEqual([1, 2, 3, 4], convert(linked_list))

    def test_singly_insert_at_head(self):
        linked_list = SingleLinkedList(SingleLLNode(2))
        linked_list.append(3)
        self.assertEqual([2, 3], convert(linked_list))
        linked_list.insert(0, 1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_singly_insert_out_of_range(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(2)
        linked_list.insert(9, 3)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_singly_delete_node_at_head(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(0)
        self.assertEqual([2, 3], convert(linked_list))

    def test_singly_delete_node_at_tail(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(2)
        self.assertEqual([1, 2], convert(linked_list))
        with self.assertRaises(IndexError):
            linked_list.delete_node(10)

    def test_singly_delete_node_in_middle(self):
        linked_list = SingleLinkedList(SingleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(1)
        self.assertEqual([1, 3], convert(linked_list))

        
class TestDoublyLinkedList(unittest.TestCase):

    def test_doubly_push_empty_list(self):
        linked_list = DoubleLinkedList()
        linked_list.push(0)
        self.assertEqual([0], convert(linked_list))

    def test_doubly_push_populated_list(self):
        linked_list = DoubleLinkedList(DoubleLLNode(2))
        linked_list.head.next = DoubleLLNode(3)
        linked_list.push(1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_doubly_append_empty_list(self):
        linked_list = DoubleLinkedList()
        linked_list.append(1)
        self.assertEqual([1], convert(linked_list))

    def test_doubly_append_populated_list(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(2)
        self.assertEqual([1, 2], convert(linked_list))

    def test_doubly_insert_empty_list(self):
        linked_list = DoubleLinkedList()
        linked_list.insert(0, 1)
        self.assertEqual([1], convert(linked_list))

    def test_doubly_insert_populated_list(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(3)
        linked_list.append(4)
        self.assertEqual([1, 3, 4], convert(linked_list))
        linked_list.insert(1, 2)
        self.assertEqual([1, 2, 3, 4], convert(linked_list))

    def test_doubly_insert_at_head(self):
        linked_list = DoubleLinkedList(DoubleLLNode(2))
        linked_list.append(3)
        self.assertEqual([2, 3], convert(linked_list))
        linked_list.insert(0, 1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_doubly_insert_out_of_range(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(2)
        linked_list.insert(9, 3)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_doubly_delete_node_at_head(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(0)
        self.assertEqual([2, 3], convert(linked_list))

    def test_doubly_delete_node_at_tail(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(2)
        self.assertEqual([1, 2], convert(linked_list))
        with self.assertRaises(IndexError):
            linked_list.delete_node(10)

    def test_doubly_delete_node_in_middle(self):
        linked_list = DoubleLinkedList(DoubleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(1)
        self.assertEqual([1, 3], convert(linked_list))

        
class TestCircularLinkedList(unittest.TestCase):

    def test_circular_push_empty_list(self):
        linked_list = CircularLinkedList()
        linked_list.push(0)
        self.assertEqual([0], convert(linked_list))

    def test_circular_push_populated_list(self):
        linked_list = CircularLinkedList(CircleLLNode(2))
        linked_list.push(1)
        self.assertEqual([1, 2], convert(linked_list))

    def test_circular_append_empty_list(self):
        linked_list = CircularLinkedList()
        linked_list.append(1)
        self.assertEqual([1], convert(linked_list))

    def test_circular_append_populated_list(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(2)
        self.assertEqual([1, 2], convert(linked_list))

    def test_circular_insert_empty_list(self):
        linked_list = CircularLinkedList()
        linked_list.insert(0, 1)
        self.assertEqual([1], convert(linked_list))

    def test_circular_insert_populated_list(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(3)
        linked_list.append(4)
        self.assertEqual([1, 3, 4], convert(linked_list))
        linked_list.insert(1, 2)
        self.assertEqual([1, 2, 3, 4], convert(linked_list))

    def test_circular_insert_at_head(self):
        linked_list = CircularLinkedList(CircleLLNode(2))
        linked_list.append(3)
        self.assertEqual([2, 3], convert(linked_list))
        linked_list.insert(0, 1)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_circular_insert_out_of_range(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(2)
        linked_list.insert(9, 3)
        self.assertEqual([1, 2, 3], convert(linked_list))

    def test_circular_delete_node_at_head(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(0)
        self.assertEqual([2, 3], convert(linked_list))

    def test_circular_delete_node_at_tail(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(2)
        self.assertEqual([1, 2], convert(linked_list))
        with self.assertRaises(IndexError):
            linked_list.delete_node(10)

    def test_circular_delete_node_in_middle(self):
        linked_list = CircularLinkedList(CircleLLNode(1))
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual([1, 2, 3], convert(linked_list))
        linked_list.delete_node(1)
        self.assertEqual([1, 3], convert(linked_list))


if __name__ == '__main__':
    unittest.main()
