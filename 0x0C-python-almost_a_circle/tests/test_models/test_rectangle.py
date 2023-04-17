#!/usr/bin/python3
"""A test case for rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 15, 3, 4, 12)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 12)

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r2 = Rectangle(5, 15, 3, 4, 12)
        self.assertEqual(r2.area(), 75)

    def test_display(self):
        r1 = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with unittest.mock.patch('sys.stdout', new=io.StringIO())\
                as fake_stdout:
            r1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

        r2 = Rectangle(4, 3, 2, 1)
        expected_output = '\n\n  ####\n  ####\n  ####\n'
        with unittest.mock.patch('sys.stdout', new=io.StringIO())\
                as fake_stdout:
            r2.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(10, 20, 5, 6, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 5/6 - 10/20')

        r2 = Rectangle(5, 15)
        self.assertEqual(str(r2), '[Rectangle] (2) 0/0 - 5/15')

    def test_update(self):
        r1 = Rectangle(10, 20, 5, 6, 12)
        r1.update(7, 4, 5, 2, 1)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

        r2 = Rectangle(5, 15, 3, 4, 12)
        r2.update(width=10, y=1, x=2, id=7)
        self.assertEqual(r2.id, 7)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 5, 6, 12)
        expected_dict = {'id': 12, 'width': 10, 'height': 20, 'x': 5, 'y': 6}
        self.assertDictEqual(r1.to_dictionary(), expected_dict)

        r2 = Rectangle(5, 15)
        expected_dict = {'id': 3, 'width': 5, 'height': 15, 'x': 0, 'y': 0}
        self.assertDictEqual(r2.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
# EnGentech sign
