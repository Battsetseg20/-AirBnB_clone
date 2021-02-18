#!/usr/bin/python3
"""Unittests for the file_storage module"""
import unittest
import models
import json
import os
from datetime import datetime

FileStorage = models.engine.file_storage.FileStorage
BaseModel = models.base_model.BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for the functionality"""
    def setUp(self):
        """Sets up the objects for testing"""
        self.storage = FileStorage()
        self.base1 = BaseModel()

    def test_instance(self):
        """Checks for the storage instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_attributes(self):
        """Checks for attributes"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """Checks if all method returns dict"""
        test_dict = models.storage.all()
        self.assertEqual(dict, type(test_dict))
        self.assertIs(test_dict, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test for the method new"""
        name_id = "{}.{}".format(type(self.base1).__name__, self.base1.id)
        test_obj = models.storage.all()
        self.assertIn(name_id, test_obj)
        self.assertEqual(self.base1, test_obj[name_id])

    def test_save(self):
        """Test for save method"""
        bm_test = BaseModel()
        bm_test.save()
        save_text = ""
        with open('file.json', 'r') as f:
            save_text = f.read()
            name_id = 'BaseModel.' + bm_test.id
            self.assertIn(name_id, save_text)

    def test_reload(self):
        """Test for reload method"""
        old_dict = self.storage.all()
        self.storage.reload()
        new_dict = self.storage.all()
        self.assertEqual(old_dict.keys(), new_dict.keys())

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
