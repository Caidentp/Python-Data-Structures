import os
import sys
import unittest

sys.path.append(os.path.split(os.getcwd())[0])

from adjacency_list import Graph


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_vertex_empty(self):
        self.graph.add_vertex(1)
        self.assertIn(1, self.graph)

    def test_add_vertex_populated(self):
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.assertIn(2, self.graph)
        self.assertIn(3, self.graph)

    def test_add_edge_no_weight(self):
        self.graph.add_edge(1, 2)
        self.assertIn(2, self.graph[1])

    def test_add_edge_with_weight(self):
        self.graph.add_edge(2, 3, 10)
        self.assertIn(3, self.graph[2])
        self.assertEqual(10, self.graph[2][3])

    def test_add_edge_invalid_first_arg(self):
        self.graph.add_edge(4, 3)
        self.assertIn(4, self.graph)
        self.assertIn(3, self.graph[4])

    def test_add_edge_invalid_second_arg(self):
        self.graph.add_edge(4, 5)
        self.assertIn(5, self.graph)
        self.assertIn(5, self.graph[4])
        

if __name__ == '__main__':
    unittest.main()