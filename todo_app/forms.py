# forms.py
from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):


    class Meta:
        model = Task
        fields = ['name', 'priority', 'category', 'start_time', 'end_time', 'status']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }