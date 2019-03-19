# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class PostTestClass(TestCase):
	def setUp(self):
		self.new_user = User.objects.create_user(username='me',password='pass1234')
		self.post = Post(post='Test Post',username=self.new_user)

	def test_instance(self):
		self.assertTrue(isinstance(self.post,Post))

	def tearDown(self):
		Post.objects.all().delete()

	def test_save_method(self):
		self.post.save_post()
		posts = Post.objects.all()
		self.assertTrue(len(posts)>0)
