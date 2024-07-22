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
            r = Rectangle(5, 0)
        self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            r = Rectangle(3, 2, 0, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_rectangle_srt(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1, "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2, "[Rectangle] (1) 1/0 - 5/5")

    def test_rectangle_display(self):
        rs = Rectangle(4, 6)
        s = """\
####    
####
####
####
####
####"""
        self.assertEqual(rs.display(), None)
        rs1 = Rectangle(3, 2, 1, 0)
        s2 = """\
 ###
 ###"""
        self.assertEqual(rs1.display(), s2)

    def test_rectangle_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r, "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(r, "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(r, "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(r, "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r, "[Rectangle] (89) 4/5 - 2/3")
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1, "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1, "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1, "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1, "[Rectangle] (89) 1/3 - 4/2")


if __name__ == "__main__":
    unittest.main()
