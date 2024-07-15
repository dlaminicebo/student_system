from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('student_number', 'first_name', 'last_name', 'email', 'password1', 'password2')
#second pdf
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'category', 'pdf_file')
