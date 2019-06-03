from django import forms
from .models import TaskCreate


class PostForm(forms.ModelForm):

    class Meta:
        model = TaskCreate
        fields = ('task_title', 'task_text', 'date')
