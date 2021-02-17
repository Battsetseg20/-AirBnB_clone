#!/usr/bin/python3
"""
Unittests for the class State
"""
import unittest
from models.base_model import BaseModel
from models.city import City

test_city = City()


class TestCityClass(unittest.TestCase):
    """Tests for the class City"""

    def test_instance(self):
        """Checks whether instance"""
        self.assertIsInstance(test_city, City)
        self.assertIsInstance(test_city, BaseModel)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertTrue(hasattr(test_city, 'state_id'))
        self.assertEqual(str, type(test_city.state_id))

        self.assertTrue(hasattr(test_city, 'name'))
        self.assertEqual(str, type(test_city.name))
