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
        pass

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
        Storage.reset()

    def test_privateclassvariableStorage(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as e:
            self.assertEqual(str(e.exception),
                             "'FileStorage' object has no" +
                             " attribute 'objects'")

    def test_privateclassvariablefilepath(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as e:
            self.assertEqual(str(e.exception),
                             "'FileStorage' object has no" +
                             " attribute 'file_path'")

    def test_attributes(self):
        '''Tests storage for attributes'''
        Storage = FileStorage()
        Storage.reset()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_storage_id(self):
        '''Tests id for Storage'''
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))
        self.assertEqual(type(b1.id), str)

    def test_storage_all_return(self):
        '''Tests that all returns dict'''
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_all(self):
        """Tests the all method of File Storage class"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        self.assertFalse(models.storage.all() == {})
        objdict = models.storage.all()
        self.assertEqual(type(objdict), dict)
        self.assertTrue("BaseModel.{}".format(b1.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b2.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b3.id) in objdict)

    def test_new(self):
        """Tests the new method of File Storage class"""
        fs = FileStorage()
        fs.new(BaseModel())
        self.assertTrue(fs.all())

    def test_new_bad(self):
        '''Tests if passing bad argument to new'''
        fs = FileStorage()
        with self.assertRaises(NameError):
            fs.new(BadModel())

    def test_new_bad_int(self):
        '''Tests if passing int to new'''
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(927)

    def test_new_bad_float(self):
        '''Tests if passing float to new'''
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(5.5)

    def test_new_bad_string(self):
        '''Tests if passing string to new'''
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new("hello")

    def test_save(self):
        """Tests the save method of File Storage class"""
        Storage = FileStorage()
        Storage.reset()
        b1 = BaseModel()
        Storage.new(b1)
        self.assertFalse(path.exists("file.json"))
        Storage.save()
        self.assertTrue(path.exists("file.json"))

    def test_savebyreadingfile(self):
        """Tests the save method by reading file"""
        Storage = FileStorage()
        Storage.reset()
        b1 = BaseModel()
        Storage.new(b1)
        Storage.save()
        with open("file.json", "r", encoding='utf-8') as r:
            content = r.read()
            self.assertTrue("BaseModel.{}".format(b1.id) in content)

    def test_reloadbyclearingdictionary(self):
        """Tests the reload method of File Storage class"""
        Storage = FileStorage()
        Storage.reset()
        b1 = BaseModel()
        Storage.new(b1)
        olddict = Storage.all()
        Storage.save()
        Storage.reset()
        Storage.reload()
        newdict = Storage.all()
        olddict = models.storage.all()
        models.storage.save()
        models.storage.reset()
        models.storage.reload()
        newdict = models.storage.all()
        for key, value in olddict.items():
            self.assertTrue(key in newdict)

    def reload_2(self):
        '''Tests reload normal'''
        Storage = FileStorage()
        b1 = BaseMode()
        Storage.new(b1)
        Storage.save()
        Storage.reset()
        Storage.reload()
        self.assertTrue(Storage.all()[BaseModel.b.id])

if __name__ == "__main__":
    unittest.main()
