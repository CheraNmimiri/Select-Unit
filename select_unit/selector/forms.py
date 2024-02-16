from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class SignupForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['birth_date'].widget = forms.widgets.DateInput(
    #         attrs={
    #             'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
    #             'class': 'form-control'
    #             }
    #     )
        
    class Meta:
        model = Student
        fields = ('full_name', 'age', 'gender', 'birth_date', 'id_number', 'phone_number', 'student_number','password' )
        widgets = {
                'birth_date': forms.DateInput(
                    attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
                )
            }
