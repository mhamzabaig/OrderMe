from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import restraunt
from .models import User
from .import forms
# Create your views here.

@login_required(login_url="res_accounts/login/")
def restraunt_intro(request):
    username = request.user.username    # Getting the user who is logged in 
    user_id = User.objects.get(username = username)     # finding that user
    Restraunt = restraunt.objects.get(res_owner = user_id)     # Finding restraunt of that user
    return render(request,'restraunts/baselayout.html',{'restraunt':Restraunt})

def edit_profile(request):
    if request.method == 'POST':
        form = forms.CreateRestraunt(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.res_owner = request.user
            instance.save()
            return redirect('restraunts:res_intro')
    else:
        form = forms.CreateRestraunt()    
    return render(request,'restraunts/edit_profile.html',{'form':form})
