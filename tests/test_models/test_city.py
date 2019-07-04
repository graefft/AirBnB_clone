#!/usr/bin/python3
'''Unittest for City class'''
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestCityClass(unittest.TestCase):
        '''This class allows for testing of City class'''

        def setUp(self):
                '''Sets up City instance for testing'''
                self.city1 = City()

        def tearDown(self):
                '''Tears down City testing'''
                pass

        def test_type(self):
                '''Tests type of City'''
                c1 = City()
                self.assertEqual(type(c1), City)

        def test_instance(self):
                '''Tests if instance of BaseModel'''
                self.assertIsInstance(self.city1, BaseModel)

        def test_City_id(self):
                '''Tests if has email attribute'''
                c1 = City()
                self.assertEqual(type(c1.id), str)
                self.assertTrue(hasattr(c1, "id"))

        def test_City_created(self):
                '''Tests created_at for City'''
                c1 = City()
                self.assertEqual(type(c1.created_at), type(datetime.now()))
                self.assertTrue(hasattr(c1, "created_at"))

        def test_City_updated(self):
                '''Tests updated_at for City'''
                c1 = City()
                self.assertEqual(type(c1.updated_at), type(datetime.now()))
                self.assertTrue(hasattr(c1, "updated_at"))

        def test_City_state_id(self):
                '''Tests state_id for City'''
                c1 = City()
                self.assertTrue(hasattr(c1, "state_id"))
                self.assertEqual(type(c1.state_id), str)

        def test_City_first_name(self):
                '''Tests name for City'''
                c1 = City()
                self.assertTrue(hasattr(c1, "name"))
                self.assertEqual(type(c1.name), str)

        def test_strmethod(self):
                '''Tets str method'''
                c1 = City()
                self.assertEqual(type(str(c1)), str)

        def test_strmethod_clsname(self):
                '''Tests if class name in str'''
                c1 = City()
                self.assertEqual('[City]' in str(c1), True)

        def test_strmethod_id(self):
                '''Tests if id is in str representation'''
                c1 = City()
                self.assertEqual('id' in str(c1), True)

        def test_str_created_City(self):
                '''Tests if created_at is in str'''
                c1 = City()
                self.assertEqual('created_at' in str(c1), True)

        def test_str_updated_City(self):
                '''Tests if updated_at is in str'''
                c1 = City()
                self.assertEqual('updated_at' in str(c1), True)

        def test_str_output_City(self):
                '''Tests for expected output'''
                c1 = City()
                output = "[{}] ({}) {}".format(
                    c1.__class__.__name__,
                    c1.id,
                    c1.__dict__
                )
                self.assertEqual(output, str(c1))

if __name__ == "__main__":
        unittest.main()
