
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from requests import post
# Create your views here.

def ResLogIn(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loginUser

            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('restraunts:res_intro')

    else:
        form = AuthenticationForm()
    
    return render(request,'res_accounts/loginform.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('res_accounts:homepage')


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