from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url="res_accounts/login/")
def restraunt_intro(request):
    return render(request,'restraunts/baselayout.html')

def edit_profile(request):
    return HttpResponse('Edit your Profile')