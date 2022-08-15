from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .forms import SignupForm
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