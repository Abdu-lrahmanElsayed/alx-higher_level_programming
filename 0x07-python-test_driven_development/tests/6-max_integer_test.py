#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_integer(unittest.TestCase):
    """The class of testing"""

    def test_max_integer(self):
        """the function to test max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 2, 6, 4]), 6)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
