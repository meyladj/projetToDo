# todo_app/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'category', 'start_time', 'end_time', 'status']
