from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'res_accounts'

urlpatterns = [
    path('', views.homepage,name = 'Home'),
    path('SignUp', views.ResSignUp,name = 'ResSignUp'),
    path('LogIn', views.ResLogIn,name = 'ResLogIn'),
        
]
