# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import SignUpForm,ProfileForm,PostsForm
from .models import Profile,Posts
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
        posts = Posts.objects.all()
        form = PostsForm()
        return render(request,'index.html',{"form":form,"posts":posts})

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
        form = ProfileForm()
        current_user=request.user
        profile = Profile.objects.get(user=current_user)
        if request.method == 'POST':
                form = ProfileForm(request.POST,request.FILES,instance=profile)
                if form.is_valid():
                        form.save()
                        return redirect('profile')
                else:
                        message = 'Fill in the form appropriately'
                        return render(request,'profile/profile.html',{"profile":profile,"form":form,"message":message})
        return render(request,'profile/profile.html',{"form":form,"profile":profile})

def posts(request):
        if request.method == 'POST':
                form = PostsForm(request.POST,request.FILES)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.user = request.user
                        post.save()
                        return redirect('index')
        return redirect('index')