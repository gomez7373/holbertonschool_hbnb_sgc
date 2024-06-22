import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="sheila.holberton@example.com", first_name="Sheila", last_name="Gomez")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "sheila.holberton@example.com")
        self.assertEqual(user.first_name, "Sheila")
        self.assertEqual(user.last_name, "Gomez")

    def test_user_to_dict(self):
        user = User(email="sheila.holberton@example.com", first_name="Sheila", last_name="Gomez")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "sheila.holberton@example.com")
        self.assertEqual(user_dict['first_name'], "Sheila")
        self.assertEqual(user_dict['last_name'], "Gomez")
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

if __name__ == '__main__':
    unittest.main()
