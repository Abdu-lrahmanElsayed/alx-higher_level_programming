#!/usr/bin/python3
"""A module for Unittest of base class"""
import unittist
from models.base import Base


class TestBase(unittest.TestCase):
    def test_initid(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)


if __name__ == '__main__':
    unittest.main()
