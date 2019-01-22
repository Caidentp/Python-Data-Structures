import os
import sys
import unittest

# add one directory up to the import path
sys.path.append(os.path.split(os.getcwd())[0])

from unrolled_linked_list_stack import Stack


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)
        self.stack.push(8)
        self.stack.push(9)
        self.stack.push(10)

    def test_initialization(self):
        s = Stack()
        self.assertEqual(s.head, None)

    def test_len_empty(self):
        s = Stack()
        self.assertEqual(len(s), 0)

    def test_push_empty(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.head.array[0], 1)
        self.assertEqual(len(s), 1)

    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_empty_empty(self):
        s = Stack()
        self.assertTrue(s.empty())

    def test_len_multiple_nodes(self):
        test = self.stack
        test.push(11)
        self.assertEqual(len(self.stack), 11)

    def test_push_full_stack(self):
        self.stack.push(11)
        self.assertEqual(self.stack.head.array[0], 11)
        self.assertEqual(self.stack.head.next.array[0], 1)
        self.assertEqual(self.stack.head.next.array[9], 10)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(len(self.stack), 10)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(len(self.stack), 9)

    def test_empty_populated(self):
        self.assertFalse(self.stack.empty())

    def test_pop_last_element_in_node(self):
        self.stack.push(10)
        self.stack.push(11)
        self.assertEqual(self.stack.pop(), 11)


if __name__ == '__main__':
    unittest.main()
