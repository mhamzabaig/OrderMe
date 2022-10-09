from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'res_accounts'

urlpatterns = [
    path('', views.homepage,name = 'Home'),
    path('Signup', views.ResSignUp,name = 'ResSignUp'),
    path('Login', views.ResLogIn,name = 'ResLogIn'),
    path('Logout', views.ResLogOut,name = 'ResLogOut'),

        
]
