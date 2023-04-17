#!/usr/bin/python3

"""A test case to check the validation of
codes written for this purpose through
EnGentech"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, '[{"id": 1, "name": "John"},\
                                    {"id": 2, "name": "Jane"}]')

    def test_save_to_file(self):
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        with open('Base.json', 'r') as file:
            json_str = file.read()
            self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

    def test_create(self):
        dict_obj = {'id': 1, 'name': 'John', 'age': 30}
        obj = Base.create(**dict_obj)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, 'John')
        self.assertEqual(obj.age, 30)

    def test_load_from_file(self):
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        objs = Base.load_from_file()
        self.assertIsInstance(objs, list)
        self.assertEqual(len(objs), 2)
        self.assertIsInstance(objs[0], Base)
        self.assertEqual(objs[0].id, 1)
        self.assertIsInstance(objs[1], Base)
        self.assertEqual(objs[1].id, 2)


if __name__ == '__main__':
    unittest.main()
# EnGentech sign
