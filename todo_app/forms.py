from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["task", "due_date", "completed"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
