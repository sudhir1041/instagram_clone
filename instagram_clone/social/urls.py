from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='Login'),
    path('Registration',Registration,name='Registration'),
    path('logout',logout,name='logout'),
    path('home',home,name='home'),
]