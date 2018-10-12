# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,email=email,password=password)
            user.save()
            profile=Profile(user=user)
            profile.save()
            login(request,user)
            return redirect('/')
    return render(request,'signup.html',{"form":form})

    
def profile(request):
        current_user=request.user
        profile = Profile.objects.get(user=current_user)
        return render(request,'profile/profile.html',{"profile":profile})
