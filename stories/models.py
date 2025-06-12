from django.db import models
from django.utils import timezone

class Story(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Story by {self.user.username} at {self.created_at}"
