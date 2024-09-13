from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class TestUserAPI(APITestCase):

    def test_register_user_success(self) -> None:
        url = reverse("user_register")
        valid_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "Qwas1287!",
            "password2": "Qwas1287!",
        }

        response = self.client.post(url, valid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self) -> None:
        url = reverse("jwt_login")
        login_valid_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "Qwas1287!",
        }
        User.objects.create_user(login_valid_data["email"], login_valid_data["password"])
        login_valid_data = {"email": login_valid_data["email"], "password": login_valid_data["password"]}

        response = self.client.post(url, login_valid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.cookies)
        self.assertIn("refresh_token", response.cookies)

    def test_logout_user(self) -> None:
        # Given
        login_url = reverse("jwt_login")
        logout_url = reverse("jwt_logout")
        login_valid_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "Qwas1287!",
        }
        User.objects.create_user(login_valid_data["email"], login_valid_data["password"])
        login_valid_data = {"email": login_valid_data["email"], "password": login_valid_data["password"]}

        # When
        login_response = self.client.post(login_url, login_valid_data, format="json")

        # Then
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", login_response.cookies)
        self.assertIn("refresh_token", login_response.cookies)

        # When
        logout_response = self.client.post(logout_url)

        # Then
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)
        self.assertEqual(logout_response.cookies["access_token"].value, "")
        self.assertEqual(logout_response.cookies["refresh_token"].value, "")
