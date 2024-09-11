from django.test import TestCase

from users.models import User


# Create your tests here.
class TestCreateUser(TestCase):

    def test_create_common_user(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234")

        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.social_type, "common")
        self.assertEqual(user.is_active, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.email_is_verified, False)

    def test_create_superuser(self) -> None:
        user = User.objects.create_superuser(email="test@test.com", password="Qwer1234")

        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.email_is_verified, True)
