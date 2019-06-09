from django import forms
from .models import FirstWord


class UploadForm(forms.ModelForm):
    class Meta:
        model = FirstWord
        fields = ['first_word']
