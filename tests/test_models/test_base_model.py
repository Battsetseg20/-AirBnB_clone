#!/usr/bin/python3
"""
Units tests for class BaseModel
"""

import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for attributes and methods """

    def setUp(self):
        """Sets up new BaseModel instance for testing"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_intance(self):
        """Checks if class is instantiated"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_instance_type(self):
        """Checks the instance type"""
        self.assertEqual(type(self.base1), BaseModel)

    def test_uuid(self):
        """Test for id"""
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)

    def test_updated_at(self):
        """Test for attribute updated_at"""
        self.assertTrue(hasattr(self.base1, 'updated_at'))
        self.assertEqual(type(self.base1.updated_at), type(datetime.now()))

    def test_created_at(self):
        """Test for attribute created_at"""
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertEqual(type(self.base1.created_at), type(datetime.now()))

    def test_str(self):
        """Test for __str__ method"""
        base1 = BaseModel()
        expected = "[BaseModel] ({}) {}".format(base1.id, base1.__dict__)
        self.assertEqual(expected, str(base1))

    def test_save(self):
        """test for save method"""
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.base1.save()
        self.assertNotEqual(self.base1.updated_at, self.base1.created_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertTrue(hasattr(BaseModel, 'to_dict'))
        base1 = BaseModel()
        dict1 = base1.to_dict()
        self.assertEqual(dict1['created_at'], base1.created_at.isoformat())
        self.assertEqual(dict1['updated_at'], base1.updated_at.isoformat())
        self.assertEqual(dict1['__class__'], 'BaseModel')

if __name__ == "__main__":
    unittest.main()
