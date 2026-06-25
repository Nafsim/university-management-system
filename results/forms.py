from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'course', 'quiz', 'forum', 'mid', 'final', 'grade']
