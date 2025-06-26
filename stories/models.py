from django.db import models
from django.utils import timezone
from accounts.models import User


class Story(models.Model):
    content= models.TextField()
    story=models.FileField(upload_to='stories/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Story  {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
