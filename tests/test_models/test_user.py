#!/usr/bin/python3
'''Unittest for User class'''
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestUserClass(unittest.TestCase):
        '''This class allows for testing of User class'''

        def setUp(self):
                '''Sets up User instance for testing'''
                self.user1 = User()

        def tearDown(self):
                '''Tears down User testing'''
                pass

        def test_type(self):
                '''Tests type of User'''
                self.assertEqual(type(self.user1), User)

        def test_instance(self):
                '''Tests if instance inherits from BaseModel'''
                self.assertIsInstance(self.user1, BaseModel)

        def test_user_id(self):
                '''Tests if has email attribute'''
                u1 = User()
                self.assertEqual(type(u1.id), str)
                self.assertTrue(hasattr(u1, "id"))

        def test_user_created(self):
                '''Tests created_at for User'''
                u1 = User()
                self.assertEqual(type(u1.created_at), type(datetime.now()))
                self.assertTrue(hasattr(self.user1, "created_at"))

        def test_user_updated(self):
                '''Tests updated_at for User'''
                u1 = User()
                self.assertEqual(type(u1.updated_at), type(datetime.now()))
                self.assertTrue(hasattr(u1, "updated_at"))

        def test_user_email(self):
                '''Tests email for User'''
                u1 = User()
                self.assertEqual(type(u1.email), str)
                self.assertTrue(hasattr(u1, "email"))

        def test_user_password(self):
                '''Tests password for User'''
                u1 = User()
                self.assertTrue(hasattr(u1, "password"))
                self.assertEqual(type(u1.password), str)

        def test_user_first_name(self):
                '''Tests first_name for User'''
                u1 = User()
                self.assertTrue(hasattr(u1, "first_name"))
                self.assertEqual(type(u1.first_name), str)

        def test_user_last_name(self):
                '''Tests last_name for User'''
                u1 = User()
                self.assertTrue(hasattr(u1, "last_name"))
                self.assertEqual(type(u1.last_name), str)

        def test_strmethod(self):
                '''Tests str method'''
                u1 = User()
                self.assertEqual(type(str(u1)), str)

        def test_strmethod_clsname(self):
                '''Tests if class name in str'''
                u1 = User()
                self.assertEqual('[User]' in str(u1), True)

        def test_strmethod_id(self):
                '''Tests if id is in str representation'''
                u1 = User()
                self.assertEqual('id' in str(u1), True)

        def test_str_created_user(self):
                '''Tests if created_at is in str'''
                u1 = User()
                self.assertEqual('created_at' in str(u1), True)

        def test_str_updated_user(self):
                '''Tests if updated_at is in str'''
                u1 = User()
                self.assertEqual('updated_at' in str(u1), True)

        def test_str_output_user(self):
                '''Tests for expected output'''
                u1 = User()
                output = "[{}] ({}) {}".format(
                    u1.__class__.__name__,
                    u1.id,
                    u1.__dict__
                )
                self.assertEqual(output, str(u1))

if __name__ == "__main__":
        unittest.main()
