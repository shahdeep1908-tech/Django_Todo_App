from django import forms
from django.utils import timezone
from .models import Todo


class TodoForm(forms.ModelForm):
    date = forms.DateTimeField(disabled=True, initial=timezone.now)

    class Meta:
        model = Todo
        fields = '__all__'
