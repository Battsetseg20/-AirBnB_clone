#!/usr/bin/python3
"""
Unittests for the class User
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Tests for the class User"""
    def test_instance(self):
        """Checks if instance"""
        test_user = User()
        self.assertIsInstance(test_user, User)
        self.assertIsInstance(test_user, BaseModel)
