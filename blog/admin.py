from django.contrib import admin

from .models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "created_at", "is_active")
    search_fields = ("user__username", "title")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)

    
