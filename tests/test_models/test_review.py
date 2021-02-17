#!/usr/bin/python3
"""
Unittests for the class State
"""
import unittest
from models.base_model import BaseModel
from models.review import Review

test_review = Review()


class TestReviewClass(unittest.TestCase):
    """Tests for the class Review"""

    def test_instance(self):
        """Checks whether instance"""
        self.assertIsInstance(test_review, Review)
        self.assertIsInstance(test_review, BaseModel)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertTrue(hasattr(test_review, 'place_id'))
        self.assertEqual(str, type(test_review.place_id))

        self.assertTrue(hasattr(test_review, 'user_id'))
        self.assertEqual(str, type(test_review.user_id))

        self.assertTrue(hasattr(test_review, 'text'))
        self.assertEqual(str, type(test_review.text))
