from django.urls import path
from .api_endpoints import *


apis = [
    path('cart/create/', CartCreateView.as_view(), name='cart-create'),
    path('cart/delete/<int:pk>/', CartDeleteView.as_view(), name='cart-delete'),
    path('cart/detail/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/item/create/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/item/delete/<int:pk>/', CartItemDeleteView.as_view(), name='cart-item-delete'),
    path('cart/item/detail/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('cart/item/list/', CartItemListView.as_view(), name='cart-item-list'),
    path('cart/item/update/<int:pk>/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('cart/list/', CartListView.as_view(), name='cart-list'),
    path('cart/update/<int:pk>/', CartUpdateView.as_view(), name='cart-update'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name="profile-delete"),

    path('password-reset/request/', PasswordResetRequestAPIView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    path('user/register/', UserRegisterAPIView.as_view(), name="user-register"),
    path('user/register/verify/', UserRegisterVerifyAPIView.as_view(), name="user-register-verify"),
    path('products/save-unsave/', SaveProductView.as_view(), name="save-unsave-products"),
    path('products/saved/', SaveProductListView.as_view(), name="saved-products"),
    

]

template_urls = [
    path("template/login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("template/logout/", SessionLogoutAPIView.as_view(), name="logout-session"),
]

urlpatterns = apis + template_urls
