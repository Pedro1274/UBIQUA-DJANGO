from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }