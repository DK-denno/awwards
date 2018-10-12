from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ['dp','bio']