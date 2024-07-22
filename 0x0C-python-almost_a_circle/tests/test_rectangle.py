#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def test_rectangle_id(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_rectangle(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 12)
        r1 = Rectangle(10, 5, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_rectangle_w_h(self):
        r = Rectangle(5, 15)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 15)

    def test_rectangle_error(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(TypeError) as e:
            r = Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, "a")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, 0, "6")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(5, -1)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(3, 2, 0, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
