from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from base.models import Tasklist
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
  
    class Meta:
        model = User
        fields =['username','email']
        labels ={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))



class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = ['title','status']