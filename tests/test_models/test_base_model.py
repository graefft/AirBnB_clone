#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel
import datetime

import unittest
class TestBaseModelClass(unittest.TestCase):
    """This class allows for testing of BaseModel class"""
    def testsingleinstancecreation(self):
        """This function tests for single instance creation"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime.datetime)
        self.assertEqual(type(b1.updated_at), datetime.datetime)
    def testmultipleinstancecreation(self):
        """This function tests for multiple instance creation"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime.datetime)
        self.assertEqual(type(b1.updated_at), datetime.datetime)
        b2 = BaseModel()
        self.assertEqual(type(b2.id), str)
        self.assertEqual(type(b2.created_at), datetime.datetime)
        self.assertEqual(type(b2.updated_at), datetime.datetime)
        b3 = BaseModel()
        self.assertEqual(type(b3.id), str)
        self.assertEqual(type(b3.created_at), datetime.datetime)
        self.assertEqual(type(b3.updated_at), datetime.datetime)
    def teststrmethod(self):
        """This function tests the str method"""
        b1 = BaseModel()
        self.assertEqual(type(str(b1)), str)
    def testsavemethod(self):
        """This function tests the save method"""
        b1 = BaseModel()
        oldtime = b1.updated_at
        b1.save()
        newtime = b1.updated_at
        self.assertNotEqual(oldtime, newtime)
    def testtodictreturntype(self):
        """This function tests the todict method"""
        b1 = BaseModel()
        self.assertEqual(type(b1.to_dict()), dict)
    def testthatclassattributeadded(self):
        """This function tests the todict method"""
        b1 = BaseModel()
        dictionary = b1.to_dict()
        self.assertEqual('__class__' in dictionary, True)
