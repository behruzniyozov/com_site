from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User

class UserRegisterTestCase(APITestCase):

    def test_register_user_success(self):
        url = reverse('user-register')  # make sure the URL name matches
        payload = {
            "email": "test@example.com",
            "password": "securePass123",
            "first_name": "John",
            "last_name": "Doe"
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_register_missing_email(self):
        url = reverse('user-register')
        payload = {
            "password": "12345678"
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_duplicate_email(self):
        User.objects.create_user(email="duplicate@example.com", password="pass1234")
        url = reverse('user-register')
        payload = {
            "email": "duplicate@example.com",
            "password": "pass5678"
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
