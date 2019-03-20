# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post,Profile
from .forms import *
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
# from .forms import ProfileForm, ProjectsForm



# Create your views here.

# def signup(request):
#    if request.method=='POST':
#        form = UserCreationForm(request.POST)

#        if form.is_valid():
#            form.save()
#        return redirect('login')
#    else:
#        form = UserCreationForm()

#    return render(request,'login.html',locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_profile(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username = current_user
            profile.save()

    else:
        form=ProfileForm()

    return render(request,'editProfile.html',{"form":form})


def index(request):
    posts = Post.objects.all()
    # form=CommentForm()

    return render(request,"index.html",{"posts":posts})

@login_required(login_url='/accounts/login/')
def userprofile(request,profile_id):
    current_user=request.user

    try:
    	all_posts=Post.objects.all()
    	profile = Profile.objects.get(id=profile_id)
    	prof_username = profile.username
    	posts = Post.objects.filter(username=prof_username)
    except:
        raise ObjectDoesNotExist()
    return render(request,"userProfile.html",{"profile":profile,"posts":posts})

@login_required(login_url='/accounts/login/')
def change_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.username = current_user
            details.save()
        return redirect('changeProfile')
    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'changeProfile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = current_user
            post.profilePhotos = profile.profilePhotos


        return redirect('newPost')

    else:
    	form = PostForm()

    return render(request, 'newPost.html',{"form":form})
        
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id

    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')

        return redirect('profile.html')

    try:
        profile = Profile.objects.get(username=current_user)
        posts = Post.objects.filter(username_id=current_user_id)
        title = profile.name
        username = profile.username
        post_number= len(posts)

    except ObjectDoesNotExist:
        return redirect('editProfile')

    return render(request,"profile.html",{"profile":profile,"posts":posts,"form":form,"post_number":post_number,"title":title,"username":username})


#@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.save()

    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})
