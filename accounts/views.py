from ast import arg
from django.urls import reverse
from contextlib import redirect_stderr
from urllib.robotparser import RequestRate
from django.shortcuts import render,redirect
from .forms import SignupForm,UserForm,ProfileForm
from .models import Profile
from django.contrib.auth import authenticate , login

# Create your views here.
def signup (request):
    
    if request.method == 'POST' :

        myform = SignupForm(request.POST)
        if myform.is_valid():
            myform.save()
            username = myform.cleaned_data['username']
            password = myform.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')

    else:
        myform = SignupForm()

    context = {
        'form':myform
    }

    return  render(request,'registration/signup.html',context)

def profile(request):

    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}

    return render(request,'accounts/profile.html',context)

def profile_edit(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST,request.FILES,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
        
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
        context = {
            'userform':userform,
            'profileform':profileform
        }
    return render(request,'accounts/profile_edit.html',context)
