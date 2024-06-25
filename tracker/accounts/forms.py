from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    email = forms.CharField(label='Email',widget= forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password',widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['email']



class LoginForm(forms.Form):
    username = forms.CharField(label='Email', max_length=100, widget= forms.EmailInput(attrs={'class': 'form-control'}))    
    password1 = forms.CharField(label='Password', max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-control'}))