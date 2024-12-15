# forms.py
from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    class Meta:
        model = Task
        fields = ['name', 'priority', 'category', 'start_time', 'end_time', 'status']
