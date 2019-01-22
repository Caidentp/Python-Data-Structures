import unittest
from test_singly import TestSinglyLinkedList
from test_doubly import TestDoublyLinkedList
from test_circular import TestCircularLinkedList


# Converts a linked list to a list for testing
def convert(linked_list):
    return [x for x in linked_list]


if __name__ == '__main__':
    unittest.main()