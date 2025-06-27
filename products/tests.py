from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from products.models import (
    Product, Brand, Category, Size, Color, ProductVariant
)


class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="admin@example.com",
            password="admin123",
            is_staff=True
        )
        self.client.login(email="admin@example.com", password="admin123")

        self.brand = Brand.objects.create(name="Apple", slug="apple")
        self.category = Category.objects.create(name="Phones", slug="phones")
        self.size = Size.objects.create(name="Large", slug="large")
        self.color = Color.objects.create(name="Black", slug="black")

        self.product = Product.objects.create(
            name="iPhone 14",
            slug="iphone-14",
            description="Latest iPhone",
            brand=self.brand,
            price=1000,
            stock=10,
            category=self.category
        )

    def test_list_products(self):
        url = reverse("products:product-list")
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        url = reverse("products:product-detail", kwargs={"slug": self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.product.name)

def test_create_product(self):
    self.client.force_login(self.user) 
    url = reverse("products:product-create")
    data = {
        "name": "iPad Pro",
        "slug": "ipad-pro",
        "description": "Latest tablet",
        "price": 1500,
        "stock": 20,
        "brand": self.brand.id,
        "category": self.category.id
    }
    response = self.client.post(url, data, format='json')  
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_brand(self):
        url = reverse("products:brand-create")
        data = {"name": "Samsung", "slug": "samsung"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_size(self):
        size = Size.objects.create(name="XL", slug="xl")
        url = reverse("products:size-delete", kwargs={"pk": size.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_product_variant(self):
        url = reverse("products:product-options-create")
        data = {
            "name": "iPhone 14 - Black Large",
            "price": 1100,
            "product": self.product.id,
            "stock": 5,
            "color": self.color.id,
            "size": self.size.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def test_create_product_review(self):
    variant = ProductVariant.objects.create(
        name="iPhone 14 Variant",
        price=1050,
        product=self.product,
        stock=5,
        color=self.color,
        size=self.size
    )
    self.client.force_login(self.user) 

    url = reverse("products:product-comment-create")
    data = {
        "product": self.product.id, 
        "rating": 5,
        "review": "Excellent quality!"
    }
    response = self.client.post(url, data)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data["rating"], 5)
    self.assertEqual(response.data["review"], "Excellent quality!")
    self.assertEqual(response.data["product"], self.product.id)



