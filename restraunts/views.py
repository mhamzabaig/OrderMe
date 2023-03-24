from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import restraunt
from .models import User
from .import forms
# Create your views here.

def GetRestraunt(request):
    
    username = request.user.username    # Getting the user who is logged in 
    user_id = User.objects.get(username = username)     # finding that user
    Restraunt = restraunt.objects.get(res_owner = user_id)     # Finding restraunt of that user
    
    return Restraunt

@login_required(login_url="res_accounts/login/")
def restraunt_intro(request):
    return render(request,'restraunts/baselayout.html',{'restraunt':GetRestraunt(request)})

def edit_profile(request):
    if request.method == 'POST':
        form = forms.CreateRestraunt(request.POST)
        
        if form.is_valid():
            instance = GetRestraunt(request)
            instance.name = request.POST['name']            
            instance.reg_id = request.POST['reg_id']            
            instance.contact_no = request.POST['contact_no']            
            instance.email_id = request.POST['email_id']
            # instance.res_owner = request.POST['res_owner']            
            instance.save()
            return redirect('restraunts:res_intro')
    else:
        form = forms.CreateRestraunt()        
    return render(request,'restraunts/edit_profile.html',{'form':form})

def completeResProfile(request):
    if request.method == 'POST':
        form = forms.CreateRestraunt(request.POST)
        form.res_owner = User.objects.get(username = request.user.username)
        
        if form.is_valid():
            form.save()
            return redirect('restraunts:res_intro')
    else:
        form = forms.CreateRestraunt()    
    return render(request,'restraunts/complete_profile.html',{'form':form})