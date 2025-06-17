from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Story

@shared_task
def delete_expired_stories():
    threshold = timezone.now() - timedelta(hours=24)
    expired = Story.objects.filter(created_at__lt=threshold)
    count = expired.count()
    expired.delete()
    return f"{count} expired stories deleted"
