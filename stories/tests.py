from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from stories.models import Story
from accounts.models import User  # adjust as needed

class StoryCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="admin@example.com",
            password="admin123",
            is_staff=True
        )
        self.client.login(email="admin@example.com", password="admin123")

    def test_create_story_text_only(self):
        url = reverse("story-create")
        data = {
            "content": "Admin's first story"
        }
        response = self.client.post(url, data, format='multipart')  # 🔧 Fix: force multipart
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 1)
        self.assertEqual(Story.objects.first().content, "Admin's first story")

    def test_create_story_with_file(self):
        url = reverse("story-create")
        file_data = SimpleUploadedFile("video.mp4", b"dummy data", content_type="video/mp4")
        data = {
            "content": "Story with video",
            "story": file_data
        }
        response = self.client.post(url, data, format='multipart')  # 🔧 Fix: force multipart
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Story.objects.filter(content="Story with video").exists())

