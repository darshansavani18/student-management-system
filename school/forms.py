from django import forms
from .models import Student, Teacher
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Student
        fields = [
            'roll_number',
            'class_name',
            'section',
            'gender',
            'date_of_birth',
            'address',
        ] 

class TeacherForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Teacher
        fields = [
            'full_name',
            'email',
            'subject',
            'phone',
        ]