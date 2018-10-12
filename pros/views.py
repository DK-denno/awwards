# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import login authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def Sigup(request):
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
            login(request,user)
    return render(request,'signup.html')

    return render('signup.html')
