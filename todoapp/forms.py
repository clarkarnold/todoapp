from django import forms
from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('text','completed','urgent')