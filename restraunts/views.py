from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def restraunt_intro(request):
    return HttpResponse('Hello my restruant ')