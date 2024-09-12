from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestRegisterUserAPI(APITestCase):

    def setUp(self) -> None:
        self.url = reverse("user_register")
        self.valid_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "Qwas1287!",
            "password2": "Qwas1287!",
        }

    def test_register_user_success(self) -> None:
        response = self.client.post(self.url, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
