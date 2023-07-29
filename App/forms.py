from django import forms
from .models import profile

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=profile
        fields=['name','image','email','age','address','phone_no','date_of_birth','religion']