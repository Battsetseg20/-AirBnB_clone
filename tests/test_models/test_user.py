#!/usr/bin/python3
"""
Unittests for the class User
"""
import unittest
import models.base_model import BaseModel
import models.user import User

class TestUserClass(unittest.TestCase):
    """Tests for the class User"""
    test_user = User()
    self.assertIsInstance(test_user, User)
    self.assertIsInstance(test_user, BaseModel)
