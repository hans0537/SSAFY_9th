from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            "issue_a": "RED TEAM",
            "issue_b": "BLUE TEAM",
        }