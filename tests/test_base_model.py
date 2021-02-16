#!/usr/bin/python3
"""
Units tests for class BaseModel
"""

import unittest
import models.base_model import BaseModel
import models
import datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Tests for attributes and methods """
    def test_uuid(self):
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base2.id), str)
