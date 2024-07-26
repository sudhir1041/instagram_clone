from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Registration(req):
    if req.method=='POST':
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get('password')

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        return redirect('Login')
    else:
        return render(req,'register.html')

def Login(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect('home')
        else:
            messages.error(req,'Invalid Credential')
            return redirect('Login')
    else:
        return render(req,'Login.html')
    
def logout(req):
    auth.logout(req)
    return redirect('/')

def profile(req):
    user=req.user
    try:
        profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
    return render(req,'Profile.html',{'profile':profile})

@login_required
def Editprofile(req):
    user=req.user
    try:
       profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile(user=user)

    if req.method == 'POST':
        profile.bio = req.POST.get('bio')
        profile.profile_picture = req.FILES.get('profile_picture')
        profile.save()
        return redirect('profile')
    return render(req, 'Editprofile.html',{'profile': profile})
    



def home(req):
    return render(req,'index.html')