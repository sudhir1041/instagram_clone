from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='Login'),
    path('Registration',Registration,name='Registration'),
    path('logout',logout,name='logout'),
    path('home',home,name='home'),
    path('profile',profile,name='profile'),
    path('Editprofile',Editprofile,name='Editprofile'),
    path('createpost',createpost,name='createpost'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
]