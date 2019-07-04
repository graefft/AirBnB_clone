#!/usr/bin/python3
'''Unittest for Amenity class'''
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestAmenityClass(unittest.TestCase):
        '''This class allows for testing of Amenity class'''

        def setUp(self):
                '''Sets up Amenity instance for testing'''
                self.amenity1 = Amenity()

        def tearDown(self):
                '''Tears down Amenity testing'''
                pass

        def test_type(self):
                '''Tests type of Amenity instance'''
                a1 = Amenity()
                self.assertEqual(type(a1), Amenity)

        def test_instance(self):
                '''Tests if instance of BaseModel'''
                self.assertIsInstance(self.amenity1, BaseModel)

        def test_amenity_id(self):
                '''Tests if has email attribute'''
                a1 = Amenity()
                self.assertEqual(type(a1.id), str)
                self.assertTrue(hasattr(a1, "id"))

        def test_amenity_created(self):
                '''Tests created_at for Amenity'''
                a1 = Amenity()
                self.assertEqual(type(a1.created_at), type(datetime.now()))
                self.assertTrue(hasattr(a1, "created_at"))

        def test_Amenity_updated(self):
                '''Tests updated_at for Amenity'''
                a1 = Amenity()
                self.assertEqual(type(a1.updated_at), type(datetime.now()))
                self.assertTrue(hasattr(a1, "updated_at"))

        def test_amenity_name(self):
                '''Tests name for Amenity'''
                a1 = Amenity()
                self.assertTrue(hasattr(a1, "name"))
                self.assertEqual(type(a1.name), str)

        def test_strmethod(self):
                '''Tets str method'''
                a1 = Amenity()
                self.assertEqual(type(str(a1)), str)

        def test_strmethod_clsname(self):
                '''Tests if class name in str'''
                a1 = Amenity()
                self.assertEqual('[Amenity]' in str(a1), True)

        def test_strmethod_id(self):
                '''Tests if id is in str representation'''
                a1 = Amenity()
                self.assertEqual('id' in str(a1), True)

        def test_str_created_Amenity(self):
                '''Tests if created_at is in str'''
                a1 = Amenity()
                self.assertEqual('created_at' in str(a1), True)

        def test_str_updated_Amenity(self):
                '''Tests if updated_at is in str'''
                a1 = Amenity()
                self.assertEqual('updated_at' in str(a1), True)

        def test_str_output_Amenity(self):
                '''Tests for expected output'''
                a1 = Amenity()
                output = "[{}] ({}) {}".format(
                    a1.__class__.__name__,
                    a1.id,
                    a1.__dict__
                )
                self.assertEqual(output, str(a1))

if __name__ == "__main__":
        unittest.main()
