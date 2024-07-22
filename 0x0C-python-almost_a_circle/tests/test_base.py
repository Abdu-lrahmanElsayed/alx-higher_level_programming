#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_base_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_base_from_json_string(self):
        self.assertEqual(
                Base.from_json_string(
                    '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]'
                    ),
                [{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]
                )
    
    def test_base_from_json_string_withnone(self):
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == "__main__":
    unittest.main()
