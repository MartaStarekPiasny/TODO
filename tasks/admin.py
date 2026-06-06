from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date", "is_completed")
    list_filter = ("status", "priority", "is_completed")
    search_fields = ("title", "description", "category")