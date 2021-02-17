#!/usr/bin/python3
"""Unittests for the file_storage module"""
import unittest
import models

FileStorage = models.engine.file_storage.FileStorage
BaseModel = models.base_model.BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests for the functionality"""
    def setUp(self):
        """Sets up the objects for testing"""
        self.storage = FileStorage()
        self.base1 = BaseModel()

    def test_intance(self):
        """Checks for the storage instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
