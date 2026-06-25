from django import forms
from django.contrib.auth import get_user_model
from django.forms import HiddenInput
from courses.models import Course

User = get_user_model()

class AdminUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'is_active', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AdminStudentForm(AdminUserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget = HiddenInput()
        self.fields['role'].initial = 'student'

class AdminTeacherForm(AdminUserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget = HiddenInput()
        self.fields['role'].initial = 'teacher'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_title', 'credit']
        widgets = {
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_title': forms.TextInput(attrs={'class': 'form-control'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control'}),
        }
