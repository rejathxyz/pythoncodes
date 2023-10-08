import unittest

# Import the function you want to test
from passord_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        # Test if the generated password has the default length of 12 characters
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        # Test if the generated password has the specified custom length
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_contains_uppercase(self):
        # Test if the generated password contains at least one uppercase letter
        password = generate_password()
        self.assertTrue(any(char.isupper() for char in password))

    def test_contains_lowercase(self):
        # Test if the generated password contains at least one lowercase letter
        password = generate_password()
        self.assertTrue(any(char.islower() for char in password))

    def test_contains_digit(self):
        # Test if the generated password contains at least one digit
        password = generate_password()
        self.assertTrue(any(char.isdigit() for char in password))

    def test_contains_special_characters(self):
        # Test if the generated password contains at least one special character
        password = generate_password()
        special_chars = string.punctuation
        self.assertTrue(any(char in special_chars for char in password))


if __name__ == "__main__":
    unittest.main()
