import os
import sys
import unittest

sys.path.append(os.path.split(os.getcwd())[0])

from adjacency_list import Graph


class TestSuite(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()