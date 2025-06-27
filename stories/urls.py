
from django.urls import path
from stories.api_endpoints import *


urlpatterns = [
    path("stories/", StoryCreateAPIView.as_view(), name="story-create"),
    path("stories/<int:pk>/", StoryListAPIView.as_view(), name="story-detail"),
    path("stories/<int:pk>/delete?", StoryDeleteAPIView.as_view(), name="story-delete"),]