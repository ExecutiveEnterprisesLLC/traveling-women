from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from posts.choices import *

# def upload_location(instance, filename):
# 	return '%s/%s' %(instance.id, filename)

class Post(models.Model):
	author = models.ForeignKey(User, null=True, blank=True)
	# title = models.CharField(max_length=120, default="")
	image = models.ImageField(null=True, blank=True)
	service = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	comments = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.location #self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp"]

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	age = models.CharField(max_length=255, choices=AGE_CHOICES, default='Pick One')
	status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pick One')
	accomplice = models.CharField(max_length=255, choices=ACCOMPLICE_CHOICES, default='Pick One')
	interests = models.CharField(max_length=255, choices=INTERESTS_CHOICES, default='Pick One')
	destinations = models.CharField(max_length=255, choices=DESTINATION_CHOICES, default='Pick One') 

	def __unicode__(self):
		return self.age