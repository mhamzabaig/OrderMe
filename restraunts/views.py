from django.shortcuts import render
# Create your views here.

def restraunt_intro(request):
    return render(request,'restraunts/res_welcome.html')