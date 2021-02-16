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

    def test_intance(self):
        """Checks if class is instantiated"""
        self.assertIsInstance(self.base1, BaseModel)

    def test_uuid(self):
        """Test for id"""
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)

    
