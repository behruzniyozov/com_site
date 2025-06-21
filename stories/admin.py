from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "story", "created_at", "is_active")
    search_fields = ("user__username", "content")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)

    # Optional: Uncomment this if you ever want to disallow adding again
    # def has_add_permission(self, request):
    #     return False