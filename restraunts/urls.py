from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'restraunts'

urlpatterns = [
    path('', views.restraunt_intro,name = 'res_intro'),
    path('edit_profile',views.edit_profile, name = 'edit'),
    path('complete_res_profile',views.completeResProfile, name = 'completeProfile'),
]
