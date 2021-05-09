#!/usr/bin/python3
"""
My Little Unittest: Testing is Lyfe
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_of_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([0, 4, 2, 6]), 6)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-7, -6, -5, -4]), -4)
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_of_floats(self):
        self.assertEqual(max_integer([0.5, 0.6, 5.5, 2.1]), 5.5)
        self.assertEqual(max_integer([-4.8, -9.1, -2.7, 0.0]), 0.0)
        self.assertEqual(max_integer([2, 1.8, 4.6, 3.1]), 4.6)

    def test_of_letters(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['c', 'c', 'd', 'c']), 'd')
        self.assertEqual(max_integer(['r', 'r', 's', 'r']), 's')

    def test_of_lists(self):
        self.assertEqual(max_integer([[1, 2, 3, 4], [3, 4, 5, 6]]), [3, 4, 5, 6])
        self.assertEqual(max_integer([[8, 7, 6, 5], [4, 3, 2, 1]]), [8, 7, 6, 5])
        self.assertEqual(max_integer([[1, 1, 1, 1], [0, 0, 0, 0]]), [1, 1, 1, 1])

    def test_of_none(self):
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
