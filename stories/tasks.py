# stories/tasks.py
from celery import shared_task
from .models import Story

@shared_task
def deactivate_story_later(story_id):
    try:
        story = Story.objects.get(id=story_id)
        story.is_active = False
        story.save()
        return f"Story {story_id} marked as inactive"
    except Story.DoesNotExist:
        return f"Story {story_id} not found"

