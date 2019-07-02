#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os

class TestBaseModelClass(unittest.TestCase):
    """This class allows for testing of BaseModel class"""

    def setUp(self):
        """Sets up BaseModel for testing"""

        self.base1 = BaseModel()

        if os.path.exists("file.json"):
            os.remove("file.json")


    def tearDown(self):
        """Tears down BaseModel testing"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_singleinstancecreation(self):
        """This function tests for single instance creation"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_different_id(self):
        """Tests for different id"""
        base1 = BaseModel(89)
        self.assertNotEqual(base1.id, 89)
        base1 = BaseModel("hello")
        self.assertNotEqual(base1.id, "hello")
        base1 = BaseModel([1, 2, 3])
        self.assertNotEqual(base1.id, [1, 2, 3])

    def test_created_at(self):
        """Tests created_at"""
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at), type(datetime.now()))
        self.assertTrue(hasattr(b1, "created_at"))

    def test_updated_at(self):
        """Tests updated_at"""
        b1 = BaseModel()
        self.assertEqual(type(b1.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(b1, "updated_at"))
        update = b1.updated_at
        self.assertTrue(update == b1.updated_at)
        b1.save()
        self.assertFalse(update == b1.updated_at)

    def test_multipleinstancecreation(self):
        """This function tests for multiple instance creation"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)
        b2 = BaseModel()
        self.assertEqual(type(b2.id), str)
        self.assertEqual(type(b2.created_at), datetime)
        self.assertEqual(type(b2.updated_at), datetime)
        b3 = BaseModel()
        self.assertEqual(type(b3.id), str)
        self.assertEqual(type(b3.created_at), datetime)
        self.assertEqual(type(b3.updated_at), datetime)
        self.assertNotEqual(b1.id, b2.id, b3.id)

    def test_addingnewattributes(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        dictionary = b1.to_dict()
        self.assertEqual('name' in dictionary, True)
        self.assertEqual('my_number' in dictionary, True)
        b2 = BaseModel()
        dictionary2 = b2.to_dict()
        self.assertEqual('name' in dictionary2, False)
        self.assertEqual('my_number' in dictionary2, False)

    def test_strmethod(self):
        """This function tests the str method"""
        b1 = BaseModel()
        self.assertEqual(type(str(b1)), str)

    def test_strmethod_clsname(self):
        '''Tests if class name in str'''
        b1 = BaseModel()
        self.assertEqual('[BaseModel]' in str(b1), True)

    def test_strmethod_id(self):
        '''Tests if id is in str representation'''
        b1 = BaseModel()
        self.assertEqual('id' in str(b1), True)

    def test_strmethod_created_at(self):
        '''Tests if created_at is in str representation'''
        b1 = BaseModel()
        self.assertEqual('created_at' in str(b1), True)

    def test_strmethod_updated_at(self):
        '''Tests if updated_at is in str representation'''
        b1 = BaseModel()
        self.assertEqual('updated_at' in str(b1), True)

    def test_strmethod_output(self):
        '''Tests for expected output'''
        b1 = BaseModel()
        output = "[{}] ({}) {}".format(
            b1.__class__.__name__,
            b1.id,
            b1.__dict__
        )
        self.assertEqual(output, str(b1))

    def test_savemethod(self):
        """This function tests the save method"""
        base1 = BaseModel()
        oldtime = base1.updated_at
        base1.save()
        newtime = base1.updated_at
        self.assertNotEqual(oldtime, newtime)

    def test_todictreturntype(self):
        """This function tests the todict method"""
        b1 = BaseModel()
        self.assertEqual(type(b1.to_dict()), dict)

    def test_thatallattributesareindict(self):
        """This function tests the todict method"""
        b1 = BaseModel()
        dictionary = b1.to_dict()
        self.assertEqual('__class__' in dictionary, True)
        self.assertEqual('id' in dictionary, True)
        self.assertEqual('created_at' in dictionary, True)
        self.assertEqual('updated_at' in dictionary, True)

    def test_invalidargumentBaseModel(self):
        """This function tests exception thrown when arg passed to BaseModel"""
        with self.assertRaises(NameError) as e:
            b1 = BaseModel(hi)
        self.assertEqual(str(e.exception), "name 'hi' is not defined")

    def test_toomanyargsforsave(self):
        """This function tests exception thrown when arg passed to save()"""
        with self.assertRaises(TypeError) as e:
            b1 = BaseModel()
            b1.save("foo")
        self.assertEqual(str(e.exception), "save() takes 1 positional" +
                                           " argument but 2 were given")

    def test_int_to_save(self):
        '''This function tests int passed to save'''

        with self.assertRaises(TypeError) as e:
            self.base1.save(89)

        b1 = BaseModel()
        with self.assertRaises(TypeError) as e:
            b1.save(89)

        self.assertEqual(str(e.exception), "save() takes 1 positional" +
                                           " argument but 2 were given")

    def test_toomanyargsfortodict(self):
        """This function tests exception thrown when arg passed to to_dict"""
        with self.assertRaises(TypeError) as e:
            b1 = BaseModel()
            b1.to_dict("foo")
        self.assertEqual(str(e.exception), "to_dict() takes 1 positional" +
                                           " argument but 2 were given")

    def test_create_from_dict(self):
        """This function tests creating base_model from dict"""
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        my_model_json = b1.to_dict()
        b2 = BaseModel(**my_model_json)
        self.assertEqual(b1.my_number, b2.my_number)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.name, b2.name)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertNotEqual(b1, b2)

if __name__ == "__main__":
    unittest.main()
