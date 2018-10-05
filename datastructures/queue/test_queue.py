from abstract_queue import *
from array_queue import *
from linked_list_queue import *

import unittest


class TestArrayQueue(unittest.TestCase):

	def test_enqueue_empty(self):
		queue = ArrayQueue()
		queue.enqueue(1)
		self.assertEqual([1], [x for x in queue])

	def test_enqueue_populated(self):
		queue = ArrayQueue()
		queue.enqueue(1)
		queue.enqueue(2)
		self.assertEqual([1, 2], [x for x in queue])

	def test_dequeue_empty(self):
		queue = ArrayQueue()
		with self.assertRaises(IndexError):
			queue.dequeue()

	def test_dequeue_populated(self):
		queue = ArrayQueue()
		queue.enqueue(1)
		queue.enqueue(2)
		self.assertEqual(1, queue.dequeue())
		self.assertEqual(2, queue.dequeue())
		with self.assertRaises(IndexError):
			queue.dequeue()

	def test_peek_empty(self):
		queue = ArrayQueue()
		with self.assertRaises(IndexError):
			queue.peek()

	def test_peek_populated(self):
		queue = ArrayQueue()
		queue.enqueue(1)
		self.assertEqual(1, queue.peek())
		self.assertEqual([1], [x for x in queue])

	def test_is_empty_empty(self):
		queue = ArrayQueue()
		self.assertTrue(queue.is_empty())

	def test_is_empty_populated(self):
		queue = ArrayQueue()
		queue.enqueue(1)
		self.assertFalse(queue.is_empty())

	def test_len(self):
		queue = ArrayQueue()
		self.assertEqual(0, len(queue))
		queue.enqueue(1)
		self.assertEqual(1, len(queue))


class TestLinkedListQueue(unittest.TestCase):

	def test_enqueue_empty(self):
		queue = LinkedListQueue()
		queue.enqueue(1)
		self.assertEqual([1], [x for x in queue])

	def test_enqueue_populated(self):
		queue = LinkedListQueue()
		queue.enqueue(1)
		queue.enqueue(2)
		self.assertEqual([1, 2], [x for x in queue])

	def test_dequeue_empty(self):
		queue = LinkedListQueue()
		with self.assertRaises(IndexError):
			queue.dequeue()

	def test_dequeue_populated(self):
		queue = LinkedListQueue()
		queue.enqueue(1)
		queue.enqueue(2)
		self.assertEqual(1, queue.dequeue())
		self.assertEqual(2, queue.dequeue())
		with self.assertRaises(IndexError):
			queue.dequeue()

	def test_peek_empty(self):
		queue = LinkedListQueue()
		with self.assertRaises(IndexError):
			queue.peek()

	def test_peek_populated(self):
		queue = LinkedListQueue()
		queue.enqueue(1)
		self.assertEqual(1, queue.peek())
		self.assertEqual([1], [x for x in queue])

	def test_is_empty_empty(self):
		queue = LinkedListQueue()
		self.assertTrue(queue.is_empty())

	def test_is_empty_populated(self):
		queue = LinkedListQueue()
		queue.enqueue(1)
		self.assertFalse(queue.is_empty())

	def test_len(self):
		queue = LinkedListQueue()
		self.assertEqual(0, len(queue))
		queue.enqueue(1)
		self.assertEqual(1, len(queue))


if __name__ == '__main__':
	unittest.main()
