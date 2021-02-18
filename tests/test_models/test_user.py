#!/usr/bin/python3
"""
Unittests for the class User
"""
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUserClass(unittest.TestCase):
    """Tests for the class User"""
    test_user = User()
    self.assertIsInstance(test_user, User)
    self.assertIsInstance(test_user, BaseModel)
