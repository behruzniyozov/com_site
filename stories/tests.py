from django.test import TestCase, override_settings
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model
from stories.models import Story
from stories.tasks import delete_expired_stories

User = get_user_model()

@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class DeleteExpiredStoriesTaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testusergmail.com', password='testpass')

        now = timezone.now()

        # Old story (older than 24 hours)
        Story.objects.create(
            content="Old story",
            created_at=now - timedelta(hours=25),
            user=self.user
        )

        # Recent story (within 24 hours)
        Story.objects.create(
            content="Recent story",
            created_at=now - timedelta(hours=2),
            user=self.user
        )

    def test_delete_expired_stories(self):
        self.assertEqual(Story.objects.count(), 2)

        result = delete_expired_stories.delay()
        result_value = result.result

        self.assertEqual(Story.objects.count(), 1)
        self.assertIn("1 expired stories deleted", result_value)





