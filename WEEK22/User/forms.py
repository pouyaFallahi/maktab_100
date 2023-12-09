from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

# class registerUser(UserCreationForm):
#     class Meta:
#         model = Users
#         fields = '__all__'

class RegisterUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
