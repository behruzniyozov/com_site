from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User, Cart

class CartTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="user@example.com", password="password123")
        self.client.login(email="user@example.com", password="password123")

    def test_create_cart_success(self):
        url = reverse('cart-create')  # confirm the URL name matches
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())

    def test_create_cart_unauthenticated(self):
        self.client.logout()
        url = reverse('cart-create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
