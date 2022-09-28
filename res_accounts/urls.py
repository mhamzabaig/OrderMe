from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'res_accoutns'

urlpatterns = [
    path('SignUp', views.ResSignUp,name = 'ResSignUp'),
    path('', views.homepage,name = 'Home'),
        
]
