import os
import sys
import unittest

sys.path.append(os.path.split(os.getcwd())[0])

from max_heap import MaxHeap
from min_heap import MinHeap


class TestMaxHeap(unittest.TestCase):
    def test_init(self):
        heap = MaxHeap()
        self.assertEqual([0], heap.heap)
        self.assertEqual(0, heap.size)

    def test_insert(self):
        heap = MaxHeap()
        heap.insert(1)
        self.assertEqual([0, 1], heap.heap)
        self.assertEqual(1, heap.heap[1])
        self.assertEqual(1, heap.size)

    def test_delete_top(self):
        heap = MaxHeap()
        heap.insert(1)
        self.assertEqual(heap.delete_top(), 1)
        self.assertEqual(0, heap.size)

    def test_perc_up(self):
        heap = MaxHeap()
        heap.insert(2)
        heap.insert(1)
        heap.insert(3)
        self.assertEqual(3, heap.heap[1])

    def test_perc_down(self):
        heap = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.delete_top()
        self.assertEqual(2, heap.heap[1])
        self.assertEqual(2, heap.size)

    def test_len(self):
        heap = MaxHeap()
        self.assertEqual(0, len(heap))
        heap.insert(1)
        self.assertEqual(1, len(heap))
        heap.delete_top()
        self.assertEqual(0, len(heap))

    def test_iter(self):
        heap = MaxHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        self.assertEqual([3, 2, 1], [x for x in heap])

    def test_from_iterable(self):
        heap = MaxHeap.from_iterable([1, 2, 3])
        self.assertEqual(3, heap.size)
        self.assertEqual(3, heap.heap[1])


class TestMinHeap(unittest.TestCase):
    def test_init(self):
        heap = MinHeap()
        self.assertEqual([0], heap.heap)
        self.assertEqual(0, heap.size)

    def test_insert(self):
        heap = MinHeap()
        heap.insert(1)
        self.assertEqual([0, 1], heap.heap)
        self.assertEqual(1, heap.heap[1])
        self.assertEqual(1, heap.size)

    def test_delete_top(self):
        heap = MinHeap()
        heap.insert(1)
        self.assertEqual(heap.delete_top(), 1)
        self.assertEqual(0, heap.size)

    def test_perc_up(self):
        heap = MinHeap()
        heap.insert(2)
        heap.insert(3)
        heap.insert(1)
        self.assertEqual(1, heap.heap[1])

    def test_perc_down(self):
        heap = MinHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.delete_top()
        self.assertEqual(2, heap.heap[1])
        self.assertEqual(2, heap.size)

    def test_len(self):
        heap = MinHeap()
        self.assertEqual(0, len(heap))
        heap.insert(1)
        self.assertEqual(1, len(heap))
        heap.delete_top()
        self.assertEqual(0, len(heap))

    def test_iter(self):
        heap = MinHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        self.assertEqual([1, 2, 3], [x for x in heap])

    def test_from_iterable(self):
        heap = MinHeap.from_iterable([1, 2, 3])
        self.assertEqual(3, heap.size)
        self.assertEqual(1, heap.heap[1])


if __name__ == '__main__':
    unittest.main()