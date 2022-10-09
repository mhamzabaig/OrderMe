from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="res_accounts/login/")
def restraunt_intro(request):
    return render(request,'restraunts/baselayout.html')