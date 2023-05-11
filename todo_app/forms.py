from .models import TodoItem
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'
