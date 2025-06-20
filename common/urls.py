from django.urls import path

from common.views import HomeView, ContactView

app_name = "common"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", ContactView.as_view(), name="blog"),
    path("blog-details/", ContactView.as_view(), name="blog-details"),
    path("shop-grid/", ContactView.as_view(), name="shop-grid"),
    path("shop-details/", ContactView.as_view(), name="shop-details"),
    path("shop-cart/", ContactView.as_view(), name="shop-cart"),
    path("about/", ContactView.as_view(), name="about"),
   
    
]