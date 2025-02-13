from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse

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
@login_required
def profile(req):
    user=req.user
    try:
        profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
    post = Post.objects.filter(user=user)
    return render(req,'Profile.html',{'profile':profile,'post':post})

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
        profile.user.username = req.POST.get('username')
        profile.save()
        profile.user.save()
        return redirect('profile')
    return render(req, 'Editprofile.html',{'profile': profile})
    
def home(req):
    user = req.user
    if user:
        profile = Profile.objects.get(user=user)
        post = Post.objects.all().order_by('-created_on')
        return render(req,'index.html',{'profile':profile,'post':post})
    else:
        return redirect('/')

def createpost(request):
    user = request.user
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        profile = Profile.objects.get(user=user)
        if image and caption:
            Post.objects.create(user=user,profile=profile, image=image, caption=caption)
            return redirect('home')
        else:
            messages.error(request, 'Add both image and caption.')
            return redirect('createpost')  
    return render(request, 'createPost.html')

@login_required
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        messages.error(request, "Post not found.")
        return redirect('home')

    user = request.user
    like, created = Like.objects.get_or_create(user=user, post=post)

    if not created:
        like.delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))