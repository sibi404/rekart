from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

CLASS_INPUT = 'block w-full rounded-md border-0 p-3 mb-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-500 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6'

LOGIN_CLASS = 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6'

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name' : 'username',
        'class' : LOGIN_CLASS
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name' : 'password',
        'class' : LOGIN_CLASS
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Username',
            'name':'username',
            'class':CLASS_INPUT
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder':'Email',
            'name':'email',
            'class':CLASS_INPUT,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Password',
            'name':'password',
            'class':CLASS_INPUT
    }))
        
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'confirm password',
            'name':'confirm_password',
            'class':CLASS_INPUT
    }))

    is_seller = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={
        'name':'is_seller',
        'class':'w-5 h-5 border-2 border-gray-300 rounded bg-gray-50 focus:ring-0'
    }))

