from django.urls import path
from api_endpoints import *

apis = [
    path('blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/list/', BlogListView.as_view(), name='blog-list'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
]
urlpatterns = apis