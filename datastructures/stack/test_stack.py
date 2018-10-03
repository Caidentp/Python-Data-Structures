from abstract_stack import *
from array_stack import *
from dynamic_array_stack import *
from linked_list_stack import *

import unittest


class TestArrayStack(unittest.TestCase):

    def test_is_full_empty_stack(self):
        stack = ArrayStack()
        self.assertFalse(stack.is_full())

    def test_is_full_full_stack(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertTrue(stack.is_full)
        with self.assertRaises(IndexError):
            stack.push(6)

    def test_length_magic_method(self):
        stack = ArrayStack()
        self.assertEqual(0, len(stack))
        stack.push(1)
        stack.push(1)
        self.assertEqual(2, len(stack))

    def test_iter_magic_method(self):
        stack = ArrayStack()
        self.assertEqual([], [x for x in stack])
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual([3, 2, 1], [x for x in stack])

    def test_pop_empty_stack(self):
        stack = ArrayStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_populated_stack(self):
        stack = ArrayStack()
        stack.push(2)
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertEqual([1, 2], [x for x in stack])

    def test_peek_empty_stack(self):
        stack = ArrayStack()
        with self.assertRaises(IndexError):
            stack.peek()


class TestDynamicArrayStack(unittest.TestCase):

    def test_length_magic_method(self):
        stack = DynamicArrayStack()
        self.assertEqual(0, len(stack))
        stack.push(1)
        stack.push(1)
        self.assertEqual(2, len(stack))

    def test_iter_magic_method(self):
        stack = DynamicArrayStack()
        self.assertEqual([], [x for x in stack])
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual([3, 2, 1], [x for x in stack])

    def test_pop_empty_stack(self):
        stack = DynamicArrayStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_populated_stack(self):
        stack = DynamicArrayStack()
        stack.push(2)
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertEqual([1, 2], [x for x in stack])

    def test_peek_empty_stack(self):
        stack = DynamicArrayStack()
        with self.assertRaises(IndexError):
            stack.peek()


class LinkedListStack(unittest.TestCase):

    def test_length_magic_method(self):
        stack = LinkedListStack()
        self.assertEqual(0, len(stack))
        stack.push(1)
        stack.push(1)
        self.assertEqual(2, len(stack))

    def test_iter_magic_method(self):
        stack = LinkedListStack()
        self.assertEqual([], [x for x in stack])
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual([3, 2, 1], [x for x in stack])

    def test_pop_empty_stack(self):
        stack = LinkedListStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_populated_stack(self):
        stack = LinkedListStack()
        stack.push(2)
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertEqual([1, 2], [x for x in stack])

    def test_peek_empty_stack(self):
        stack = LinkedListStack()
        with self.assertRaises(IndexError):
            stack.peek()


if __name__ == '__main__':
    unittest.main()