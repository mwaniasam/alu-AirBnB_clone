import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.test_file = "test_file.json"
        models.storage.file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        Clean up after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        """
        Test default attributes of User instances.
        """
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_base_model(self):
        """
        Test if User class inherits from BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        """
        Test the string representation of a User instance.
        """
        test_user = User(
            email="mwania@example.com",
            first_name="Samuel",
            last_name="Mwania",
            password="password654321"
        )
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("mwania@example.com", user_str)
        self.assertIn("Samuel", user_str)
        self.assertIn("Mwania", user_str)

    def test_user_to_dict(self):
        """
        Test dictionary representation of a User instance.
        """
        test_user = User(
            email="mwania@example.com",
            first_name="Samuel",
            last_name="Mwania"
        )
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "mwania@example.com")
        self.assertEqual(user_dict['first_name'], "Samuel")
        self.assertEqual(user_dict['last_name'], "Mwania")

    def test_user_instance_creation(self):
        """
        Test User instance creation with custom attributes.
        """
        test_user = User(
            email="mwania@example.com",
            password="password654321",
            first_name="Samuel",
            last_name="Mwania"
        )
        self.assertEqual(test_user.email, "mwania@example.com")
        self.assertEqual(test_user.password, "password654321")
        self.assertEqual(test_user.first_name, "Samuel")
        self.assertEqual(test_user.last_name, "Mwania")

    def test_user_instance_to_dict(self):
        """
        Test converting a User instance to a dictionary.
        """
        test_user = User(
            email="mwania@example.com",
            password="password654321",
            first_name="Samuel",
            last_name="Mwania"
        )
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "mwania@example.com")
        self.assertEqual(user_dict['password'], "password654321")
        self.assertEqual(user_dict['first_name'], "Samuel")
        self.assertEqual(user_dict['last_name'], "Mwania")

    def test_user_id_generation(self):
        """
        Test that each User instance gets a unique ID.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

if __name__ == "__main__":
    unittest.main()
