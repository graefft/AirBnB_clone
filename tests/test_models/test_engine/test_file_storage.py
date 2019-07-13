#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import models
import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path
import os
from datetime import datetime


class TestFileStorageClass(unittest.TestCase):
    """This class enables testing of FileStorage class"""

    def setUp(self):
        """Defines instructions that will be executed before each test"""
        pass

    def tearDown(self):
        """Defines instructions that will be executed after each test"""
        if os.path.exists("file.json"):
            os.rename("file.json", "foo")

    def test_instancecreation(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        self.assertTrue(type(Storage) == FileStorage)
        self.assertTrue(isinstance(Storage, FileStorage))

    def test_privateclassvariableStorage(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as e:
            print(Storage.__objects)
        self.assertEqual(str(e.exception),
                         "'FileStorage' object has no" +
                         " attribute '_TestFileStorageClass__objects'")

    def test_privateclassvariablefilepath(self):
        """Test that instance of FileStorage is properly created"""
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as e:
            print(Storage.__file_path)
        self.assertEqual(str(e.exception),
                         "'FileStorage' object has no" +
                         " attribute '_TestFileStorageClass__file_path'")

    def test_attributes(self):
        '''Tests storage for attributes'''
        Storage = FileStorage()
        Storage.reset()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_instanceattributes(self):
        '''Tests storage for attributes'''
        Storage = FileStorage()
        Storage.reset()
        self.assertTrue(hasattr(Storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(Storage, "_FileStorage__objects"))

    def test_storage_all_return(self):
        '''Tests that all returns dict'''
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_all(self):
        """Tests the all method of File Storage class"""
        Storage = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        Storage.new(b1)
        Storage.new(b2)
        Storage.new(b3)
        objdict = Storage.all()
        self.assertEqual(type(objdict), dict)
        self.assertFalse(objdict == {})
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
        b1 = BaseModel()
        Storage.new(b1)
        olddict = Storage.all()
        Storage.save()
        Storage.reset()
        Storage.reload()
        newdict = Storage.all()
        for key, value in olddict.items():
            self.assertTrue(key in newdict)

    def test_reload_2(self):
        '''Tests reload normal'''
        Storage = FileStorage()
        b1 = BaseModel()
        Storage.new(b1)
        Storage.save()
        Storage.reset()
        Storage.reload()
        self.assertTrue(Storage.all()["BaseModel.{}".format(b1.id)])
        self.assertTrue(Storage._FileStorage__objects["BaseModel.{}".
                                                      format(b1.id)])

    def test_reload(self):
        '''Tests reload'''
        Storage = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        objdict = Storage.all()
        b1.save()
        Storage.reload()
        objdict_resave = Storage.all()
        self.assertTrue(objdict == objdict_resave)

    def test_reload_update_and_create(self):
        '''Tests if updated and created are the same'''
        f1 = FileStorage()
        b1 = BaseModel()
        f1.new(b1)
        all_objs = f1.all()
        for key, value in all_objs.items():
            if key == "BaseModel.{}".format(b1.id):
                self.assertFalse(value.created_at == value.updated_at)

    def test_json_reload_times(self):
        '''Tests updated and created are same for json'''
        f1 = FileStorage()
        b1 = BaseModel()
        f1.reset()
        f1.new(b1)
        bcreate = datetime.isoformat(b1.created_at)
        bupdate = datetime.isoformat(b1.updated_at)
        f1.save()
        with open("file.json", "r", encoding='utf-8') as f:
            content = f.read()
            self.assertTrue(bcreate in content)
            self.assertTrue(bupdate in content)
    
    def test_reload_3(self):
        '''Tests reload again'''
        FileStorage().reset()
        b1 = BaseModel()
        u1 = User()
        c1 = City()
        s1 = State()
        a1 = Amenity()
        p1 = Place()
        r1 = Review()
        FileStorage().save()
        FileStorage._FileStorage__objects = {}
        FileStorage().reload()
        fso = FileStorage._FileStorage__objects
        bid = "BaseModel." + b1.id
        cid = "City." + c1.id
        uid = "User." + u1.id
        sid = "State." + s1.id
        aid = "Amenity." + a1.id
        pid = "Place." + p1.id
        rid = "Review." + r1.id
        self.assertIn(bid, fso)
        self.assertIn(cid, fso)
        self.assertIn(uid, fso)
        self.assertIn(sid, fso)
        self.assertIn(aid, fso)
        self.assertIn(pid, fso)
        self.assertIn(rid, fso)


if __name__ == "__main__":
    unittest.main()
