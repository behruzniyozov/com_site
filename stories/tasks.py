# stories/tasks.py
from celery import shared_task
from .models import Story

@shared_task
def deactivate_story_later(story_id):
    print(f"Task started for story {story_id}")
    try:
        story = Story.objects.get(id=story_id)
        story.is_active = False
        story.save()
        print(f"Story {story_id} deactivated")
    except Story.DoesNotExist:
        print(f"Story {story_id} not found")


