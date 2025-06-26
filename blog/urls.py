from django.urls import path
from blog.api_endpoints import *
from blog.views import blog_list_view

app_name = 'blog'

apis = [
    path('blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/list/', BlogListView.as_view(), name='blog-list'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
]

urls= [
    path('blog/', blog_list_view, name='blog-list-view'),
]
urlpatterns = apis + urls