#!/usr/bin/python3
'''Unittest for State class'''
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestStateClass(unittest.TestCase):
        '''This class allows for testing of State class'''

        def setUp(self):
                '''Sets up State for testing'''
                self.state1 = State()

        def tearDown(self):
                '''Tears down State testing'''
                pass

        def test_type(self):
                '''Tests type of State'''
                self.assertEqual(type(self.state1), State)

        def test_instance(self):
                '''Tests if instance of BaseModel'''
                self.assertIsInstance(self.state1, BaseModel)

        def test_state_id(self):
                '''Tests if has email attribute'''
                s1 = State()
                self.assertEqual(type(s1.id), str)
                self.assertTrue(hasattr(s1, "id"))

        def test_state_created(self):
                '''Tests created_at for State'''
                s1 = State()
                self.assertEqual(type(s1.created_at), type(datetime.now()))
                self.assertTrue(hasattr(self.state1, "created_at"))

        def test_state_updated(self):
                '''Tests updated_at for State'''
                s1 = State()
                self.assertEqual(type(s1.updated_at), type(datetime.now()))
                self.assertTrue(hasattr(s1, "updated_at"))

        def test_state_name(self):
                '''Tests name for State'''
                s1 = State()
                self.assertTrue(hasattr(s1, "name"))
                self.assertEqual(type(s1.name), str)

        def test_strmethod(self):
                '''Tests str method'''
                s1 = State()
                self.assertEqual(type(str(s1)), str)

        def test_strmethod_clsname(self):
                '''Tests if class name in str'''
                s1 = State()
                self.assertEqual('[State]' in str(s1), True)

        def test_strmethod_id(self):
                '''Tests if id is in str representation'''
                s1 = State()
                self.assertEqual('id' in str(s1), True)

        def test_str_created_state(self):
                '''Tests if created_at is in str'''
                s1 = State()
                self.assertEqual('created_at' in str(s1), True)

        def test_str_updated_state(self):
                '''Tests if updated_at is in str'''
                s1 = State()
                self.assertEqual('updated_at' in str(s1), True)

        def test_str_output_state(self):
                '''Tests for expected output'''
                s1 = State()
                output = "[{}] ({}) {}".format(
                    s1.__class__.__name__,
                    s1.id,
                    s1.__dict__
                )
                self.assertEqual(output, str(s1))

if __name__ == "__main__":
        unittest.main()
