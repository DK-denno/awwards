# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import modelformset_factory
from django.shortcuts import render,redirect
from .forms import SignUpForm,ProfileForm,PostsForm,ImageForm
from .models import Profile,Images
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
        postForm = PostsForm()
        ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=4)
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'index.html',{'postForm': postForm, 'formset': formset})

      
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
        ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=4)

        if request.method == 'POST':
                postform = PostsForm(request.POST)
                formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
                if postForm.is_valid() and formset.is_valid():
                        post_form = postform.save(commit=False)
                        post_form.user = request.user
                        post_form.save()
                for form in formset.cleaned_data:
                        image = form['image']
                        photo = Images(post=post_form, image=image)
                        photo.save()
                        return redirect('index')
        return redirect('index')