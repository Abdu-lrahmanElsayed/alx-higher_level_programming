#!/usr/bin/python3
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)


if __name__ == "__main__":
    unittest.main()
