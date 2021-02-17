#!/usr/bin/python3
"""
Unittests for the class Amenity
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

test_amenity = Amenity()


class TestAmenityClass(unittest.TestCase):
    """Tests for the class Amenity"""

    def test_instance(self):
        """Checks whether instance"""
        self.assertIsInstance(test_amenity, Amenity)
        self.assertIsInstance(test_amenity, BaseModel)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertTrue(hasattr(test_amenity, 'name'))
        self.assertEqual(str, type(test_amenity.name))
