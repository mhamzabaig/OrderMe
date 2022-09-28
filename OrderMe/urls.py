
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restraunt/', include('restraunts.urls')),
    path('res_accounts/', include('res_accounts.urls')),
    path('', views.homepage),
]
