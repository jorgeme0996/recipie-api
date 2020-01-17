from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'ejemplo@ejemplo.com'
        password = '1234567989'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for new user is normalized"""
        email = "ejemplo@EJEMPPLO.COM"
        user = get_user_model().objects.create_user(email, '123456789')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test user with email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_super_user_is_created(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'ejemplo@ejemplo.com',
            'test123456789'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)