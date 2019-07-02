#!/usr/bin/python3
'''Unittest for review class'''
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestreviewClass(unittest.TestCase):
        '''This class allows for testing of review class'''

        def setUp(self):
                '''Sets up review for testing'''
                self.review1 = Review()

        def tearDown(self):
                '''Tears down review testing'''
                pass

        def test_type(self):
                '''Tests type of review'''
                self.assertEqual(type(self.review1), Review)

        def test_instance(self):
                '''Tests if instance of BaseModel'''
                self.assertIsInstance(self.review1, BaseModel)

        def test_review_id(self):
                '''Tests if has email attribute'''
                r1 = Review()
                self.assertEqual(type(r1.id), str)
                self.assertTrue(hasattr(r1, "id"))

        def test_review_created(self):
                '''Tests created_at for review'''
                r1 = Review()
                self.assertEqual(type(r1.created_at), type(datetime.now()))
                self.assertTrue(hasattr(self.review1, "created_at"))

        def test_review_updated(self):
                '''Tests updated_at for review'''
                r1 = Review()
                self.assertEqual(type(r1.updated_at), type(datetime.now()))
                self.assertTrue(hasattr(r1, "updated_at"))

        def test_review_user_id(self):
                '''Tests user id for review'''
                r1 = Review()
                self.assertTrue(hasattr(r1, "user_id"))
                self.assertEqual(type(r1.user_id), str)

        def test_review_place_id(self):
                '''Tests review for place id'''
                r1 = Review()
                self.assertTrue(hasattr(r1, "place_id"))
                self.assertEqual(type(r1.place_id), str)

        def test_review_txt(self):
                '''Tests text for review'''
                r1 = Review()
                self.assertTrue(hasattr(r1, "text"))
                self.assertEqual(type(r1.text), str)

        def test_strmethod(self):
                '''Tests str method'''
                r1 = Review()
                self.assertEqual(type(str(r1)), str)

        def test_strmethod_clsname(self):
                '''Tests if class name in str'''
                r1 = Review()
                self.assertEqual('[Review]' in str(r1), True)

        def test_strmethod_id(self):
                '''Tests if id is in str representation'''
                r1 = Review()
                self.assertEqual('id' in str(r1), True)

        def test_str_created_review(self):
                '''Tests if created_at is in str'''
                r1 = Review()
                self.assertEqual('created_at' in str(r1), True)

        def test_str_updated_review(self):
                '''Tests if updated_at is in str'''
                r1 = Review()
                self.assertEqual('updated_at' in str(r1), True)

        def test_str_output_review(self):
                '''Tests for expected output'''
                r1 = Review()
                output = "[{}] ({}) {}".format(
                    r1.__class__.__name__,
                    r1.id,
                    r1.__dict__
                )
                self.assertEqual(output, str(r1))

if __name__ == "__main__":
        unittest.main()
