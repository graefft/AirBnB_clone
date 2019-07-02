#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from os import path
import os


class TestFileStorageClass(unittest.TestCase):
    """This class allows for testing of FileStorage class"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        Storage = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        objdict = Storage.all()
        self.assertEqual(type(objdict), dict)
        for k, v in objdict.items():
            self.assertEqual(type(v), BaseModel)

    def test_new(self):
        Storage = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        objdict = Storage.all()
        self.assertTrue("BaseModel.{}".format(b1.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b2.id) in objdict)
        self.assertTrue("BaseModel.{}".format(b3.id) in objdict)
        self.assertFalse("BaseMod.{}".format(b3.id) in objdict)

    def test_save(self):
        Storage = FileStorage()
        b1 = BaseModel()
        self.assertFalse(path.exists("file.json"))
        b1.save()
        self.assertTrue(path.exists("file.json"))

    def test_reload(self):
        Storage = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        objdict = Storage.all()
        b1.save()
        Storage.reload()
        objdict_resave = Storage.all()
        self.assertTrue(objdict == objdict_resave)
