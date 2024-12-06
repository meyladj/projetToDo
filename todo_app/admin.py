# todo_app/admin.py

from django.contrib import admin
from .models import Task, TaskList

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'category', 'start_time', 'end_time', 'status')
    list_filter = ('priority', 'status', 'category')
    search_fields = ('name', 'category')

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
