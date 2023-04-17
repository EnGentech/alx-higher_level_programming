#!/usr/bin/python3

import unittest
from models.base import Base

"""A test case written for base"""


class TestBase(unittest.TestCase):
    """class definition for base test case"""

    def test_saving_id(self):
        """test case for base with 100 value"""

        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_initialization(self):
        """second test case"""

        chk1 = Base()
        chk2 = Base()
        self.assertEqual(chk1.id, 1)
        self.assertEqual(chk2.id, 2)

    def test_to_json_string_valid(self):
        """no test case"""

        pass


if __name__ == '__main__':
    unittest.main()

# EnGentech sign
