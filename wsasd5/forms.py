from django import forms
from .models import Position

class EmployeeForm(forms.Form):
        employee_firstname = forms.CharField(label='First Name:', max_length = 100)
        employee_lastname = forms.CharField(label='Last Name:', max_length = 100)
        employee_id = forms.CharField(label='ID Number:', max_length = 10)
        employee_cv = forms.FileField(required=False)
        employee_photo = forms.ImageField(required=False)
        employee_dob = forms.DateField(required=False)
        employee_position = forms.ModelChoiceField(queryset=Position.objects.all())
