# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

import datetime as dt

# Create your models here.
Gender=(
    ('Male','Male'),
    ('Female','Female'),
    )

class Profile(models.Model):
    profilePhotos = models.ImageField(upload_to='media/profilePhotos/')
    bio = HTMLField()
    name = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField()
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=15,choices=Gender,default="Male")

    def __str__(self):
        return self.username


    
@classmethod
def search_by_profile(cls,search_term):
#__icontains searches for matches of search term(s)
    awwward = cls.objects.filter(title__icontains=search_term)
    return awwward

	# def __str__(self):
	# 	self.save = username

@classmethod
def search_profile(cls,search_term):
    profiles = cls.objects.filter(Q(username__username=search_term) | Q(name__icontains=search_term))


class Post(models.Model):
    # profile_picture = models.ImageField(upload_to = 'media/profilephotos/')
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ImageField(upload_to='posts/')
    # likes = models.IntegerField()

    # location = models.ForeignKey(Location,on_delete=models.CASCADE)

    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    def save_post(self):
    	self.save()

    @classmethod
    def delete_post(cls,location):
        cls.objects.filter(location=location).delete()

		
