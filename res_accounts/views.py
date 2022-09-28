from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ResSignUp(request):
    return HttpResponse('lets get this bastard account')

def homepage(request):
    return HttpResponse('Hey this is homepage of a restraunt')