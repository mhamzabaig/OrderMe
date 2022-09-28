from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ResSignUp(request):
    return HttpResponse('lets get this bastard account')

def homepage(request):
    return render(request,'res_accounts/homepage.html')