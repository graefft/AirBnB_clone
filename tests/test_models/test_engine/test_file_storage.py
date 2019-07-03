#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import models
import unittest
from models.base_model import BaseModel
from os import path
import os


class TestFileStorageClass(unittest.TestCase):
    """This class enables testing of FileStorage class"""

    def setUp(self):
        """Defines instructions that will be executed before each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        models.storage.reset()

    def tearDown(self):
        """Defines instructions that will be executed after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        models.storage.reset()

    def test_instancecreation(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        self.assertTrue(type(Storage) == FileStorage)
        self.assertTrue(isinstance(Storage, FileStorage))

    def test_all(self):
        """Tests the all method of File Storage class"""
        self.assertTrue(models.storage.all() == {})
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        self.assertFalse(models.storage.all() == {})
        objdict = models.storage.all()
        self.assertEqual(type(objdict), dict)
        for k, v in objdict.items():
            self.assertEqual(type(v), BaseModel)
        self.assertTrue("BaseModel.{}".format(b1.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b2.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b3.id) in objdict)

    def test_new(self):
        """Tests the new method of File Storage class"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        objdict = models.storage.all()
        self.assertTrue("BaseModel.{}".format(b1.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b2.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b3.id) in objdict)
        self.assertFalse("BaseMod.{}".format(b3.id) in objdict)

    def test_save(self):
        """Tests the save method of File Storage class"""
        b1 = BaseModel()
        self.assertFalse(path.exists("file.json"))
        b1.save()
        self.assertTrue(path.exists("file.json"))

    def test_savebyreadingfile(self):
        """Tests the save method by reading file"""
        b1 = BaseModel()
        b1.save()
        with open("file.json", "r", encoding='utf-8') as r:
            content = r.read()
            self.assertTrue("BaseModel.{}".format(b1.id) in content)

    def test_reloadbyclearingdictionary(self):
        """Tests the reload method of File Storage class"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        olddict = models.storage.all()
        models.storage.save()
        models.storage.reset()
        models.storage.reload()
        newdict = models.storage.all()
        for key, value in olddict.items():
            self.assertTrue(key in newdict)

if __name__ == "__main__":
    unittest.main()
