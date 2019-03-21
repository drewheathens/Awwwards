# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):
	def setUp(self):
		self.new_user = User.objects.create_user(username='me',password='pass1234')
		self.profile = Profile(profile='Test Profile',username=self.new_user)

	def test_instance(self):
		self.assertTrue(isinstance(self.projct,Profile))

	def tearDown(self):
		Profile.objects.all().delete()

	def test_save_method(self):
		self.post.save_post()
		profile = Profile.objects.all()
		self.assertTrue(len(profile)>0)
