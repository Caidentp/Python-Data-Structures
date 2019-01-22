import os
import sys
import unittest

sys.path.append(os.path.split(os.getcwd())[0])

from hashtable import *


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(10)
        self.table.put('a', 1)
        self.table.put('b', 2)
        self.table.put('c', 3)
        self.table.put('d', 4)
        self.table.put('aa', 5)
        self.table.put('bb', 6)
        self.table.put('cc', 7)
        self.table.put('dd', 8)

    def test_permutation_hashes(self):
        self.assertNotEqual(self.table._hash_function('abc'),
                            self.table._hash_function('cba'))

    def test_len(self):
        self.assertEqual(len(self.table), 8)

    def test_getitem(self):
        self.assertEqual(self.table['a'], 1)
        self.assertEqual(self.table['b'], 2)
        self.assertEqual(self.table['c'], 3)
        self.assertEqual(self.table['d'], 4)
        self.assertEqual(self.table['aa'], 5)
        self.assertEqual(self.table['bb'], 6)
        self.assertEqual(self.table['cc'], 7)
        self.assertEqual(self.table['dd'], 8)

    def test_setitem(self):
        self.table['a'] = 8
        self.table['b'] = 7
        self.table['c'] = 6
        self.table['d'] = 5
        self.assertEqual(self.table['a'], 8)
        self.assertEqual(self.table['b'], 7)
        self.assertEqual(self.table['c'], 6)
        self.assertEqual(self.table['d'], 5)

    def test_delete_existing_item(self):
        self.table.delete('aa')
        self.table.delete('bb')
        self.table.delete('cc')
        self.table.delete('dd')
        self.assertEqual(len(self.table), 4)

    def test_delete_nonexisting_item(self):
        self.table.delete('ee')
        self.assertEqual(len(self.table), 8)

    def test_delete_table(self):
        self.table.delete('a')
        self.table.delete('b')
        self.table.delete('c')
        self.table.delete('d')
        self.table.delete('aa')
        self.table.delete('bb')
        self.table.delete('cc')
        self.table.delete('dd')
        self.assertEqual(self.table.table, [None]*10)


if __name__ == '__main__':
    unittest.main()
