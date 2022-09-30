
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from requests import post
# Create your views here.

def ResSignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('restraunts:res_intro')
    else: 
        form = UserCreationForm()
    return render(request,'res_accounts/signupform.html',{'form':form})


def homepage(request):
    return render(request,'res_accounts/homepage.html')