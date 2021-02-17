#!/usr/bin/python3
"""
Unittests for the class State
"""
import unittest
from models.base_model import BaseModel
from models.place import Place

test_place = Place()


class TestPlaceClass(unittest.TestCase):
    """Tests for the class User"""

    def test_instance(self):
        """Checks whether instance"""
        self.assertIsInstance(test_place, Place)
        self.assertIsInstance(test_place, BaseModel)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertTrue(hasattr(test_place, 'city_id'))
        self.assertEqual(str, type(test_place.city_id))

        self.assertTrue(hasattr(test_place, 'name'))
        self.assertEqual(str, type(test_place.name))

        self.assertTrue(hasattr(test_place, 'user_id'))
        self.assertEqual(str, type(test_place.user_id))

        self.assertTrue(hasattr(test_place, 'description'))
        self.assertEqual(str, type(test_place.description))

        self.assertTrue(hasattr(test_place, 'number_rooms'))
        self.assertEqual(int, type(test_place.number_rooms))

        self.assertTrue(hasattr(test_place, 'number_bathrooms'))
        self.assertEqual(int, type(test_place.number_bathrooms))

        self.assertTrue(hasattr(test_place, 'max_guest'))
        self.assertEqual(int, type(test_place.max_guest))

        self.assertTrue(hasattr(test_place, 'price_by_night'))
        self.assertEqual(int, type(test_place.price_by_night))

        self.assertTrue(hasattr(test_place, 'latitude'))
        self.assertEqual(float, type(test_place.latitude))

        self.assertTrue(hasattr(test_place, 'longitude'))
        self.assertEqual(float, type(test_place.longitude))

        self.assertTrue(hasattr(test_place, 'amenity_ids'))
        self.assertEqual(list, type(test_place.amenity_ids))
