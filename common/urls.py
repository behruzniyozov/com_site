from django.urls import path
from .views import *



urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    
    # Contact page view (GET)
    path("contact/", ContactView.as_view(), name="contact"),

    # Contact form handler (POST only)
    path("contact/submit/", contact_message_handler, name="contact-message-handler"),

    # Other placeholders
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog-details/", ContactView.as_view(), name="blog-details"),
    path("shop-grid/", ContactView.as_view(), name="shop-grid"),
    path("shop-details/", ContactView.as_view(), name="shop-details"),
    path("shop-cart/", ContactView.as_view(), name="shop-cart"),
    path("about/", ContactView.as_view(), name="about"),
    # path("checkout/", CheckoutView.as_view(), name="checkout"),
    path('checkout/', checkout_view, name='checkout'),
    path("product/<slug:slug>/", product_detail_view, name="product-detail"),
]


   
    
