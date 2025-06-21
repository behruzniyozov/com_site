from django.db import models
from django.utils import timezone
from accounts.models import User


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    content= models.TextField()
    story=models.FileField(upload_to='stories/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Story by {self.user.email} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
