from django.urls import path
from products.api_endpoints import *


app_name = 'products'


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brands/update/<int:pk>/', BrandUpdateView.as_view(), name='brand-update'),
    path('brands/delete/<int:pk>/', BrandDeleteView.as_view(), name='brand-delete'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('sizes/create/', SizeCreateView.as_view(), name='size-create'),
    path('sizes/update/<int:pk>/', SizeUpdateView.as_view(), name='size-update'),
    path('sizes/delete/<int:pk>/', SizeDeleteView.as_view(), name='size-delete'),
    path('sizes/', SizeListView.as_view(), name='size-list'),
    path('colors/create/', ColorCreateView.as_view(), name='color-create'),
    path('colors/update/<int:pk>/', ColorUpdateView.as_view(), name='color-update'),
    path('colors/delete/<int:pk>/', ColorDeleteView.as_view(), name='color-delete'),
    path('colors/', ColorListView.as_view(), name='color-list'),
    path('product-options/create/', ProductOptionCreateView.as_view(), name='product-options-create'),
    path('product-options/update/<int:pk>/', ProductOptionUpdateView.as_view(), name='product-options-update'),
    path('product-options/delete/<int:pk>/', ProductOptionDeleteView.as_view(), name='product-options-delete'),
    path('product-options/', ProductOptionsListView.as_view(), name='product-options-list'),
    path('product-options/<int:pk>/', ProductOptionDetailView.as_view(), name='product-options-detail'),

]