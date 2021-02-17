#!/usr/bin/python3
"""
Unittests for the class State
"""
import unittest
from models.base_model import BaseModel
from models.state import State

test_state = State()


class TestStateClass(unittest.TestCase):
    """Tests for the class User"""

    def test_instance(self):
        """Checks whether instance"""
        self.assertIsInstance(test_state, State)
        self.assertIsInstance(test_state, BaseModel)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertTrue(hasattr(test_state, 'name'))
        self.assertEqual(str, type(test_state.name))
