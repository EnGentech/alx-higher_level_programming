#!/usr/bin/python3
"""A test case for Square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(10, 2, 3, 4)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -5

    def test_str(self):
        s1 = Square(5, 1, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 1/2 - 5")

    def test_update(self):
        s1 = Square(5, 1, 2, 3)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 1/2 - 5")
        s1.update(10, 20)
        self.assertEqual(str(s1), "[Square] (10) 1/2 - 20")
        s1.update(10, 20, 30)
        self.assertEqual(str(s1), "[Square] (10) 30/2 - 20")
        s1.update(10, 20, 30, 40)
        self.assertEqual(str(s1), "[Square] (10) 30/40 - 20")

    def test_to_dict(self):
        s1 = Square(5, 1, 2, 3)
        s1_dict = {'id': 3, 'size': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(s1.to_dictionary(), s1_dict)

    def test_from_dict(self):
        s1 = Square(5, 1, 2, 3)
        s1_dict = {'id': 3, 'size': 5, 'x': 1, 'y': 2}
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))


if __name__ == '__main__':
    unittest.main()

# EnGentech sign
