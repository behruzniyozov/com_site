from django.urls import path
from .api_endpoints import *

urlpatterns = [
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
]
