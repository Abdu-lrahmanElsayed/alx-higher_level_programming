#!/usr/bin/python3
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()
