from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import restraunt
from .models import User
# Create your views here.

@login_required(login_url="res_accounts/login/")
def restraunt_intro(request):
    username = request.user.username
    user_id = User.objects.get(username = username)
    Restraunt = restraunt.objects.get(res_owner = user_id)
    print(Restraunt.name)    
    return render(request,'restraunts/baselayout.html',{'restraunt':Restraunt})

def edit_profile(request):
    return HttpResponse('Edit your Profile')