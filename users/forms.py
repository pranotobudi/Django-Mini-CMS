from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm   
from .models import Profile 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #additional field aside from User model (username, password) which is choosen below

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
