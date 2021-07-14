from django.contrib.auth.models import User
from django.db import models

from thirty.posts.constants import Distinction
from thirty.posts.models import Post


class Profile(models.Model):
	username = models.CharField(max_length=50, unique=True)
	distinction = models.CharField(max_length=50, choices=Distinction.choices)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	bio = models.CharField(max_length=255, blank=True)
	friends = models.ManyToManyField("Profile", blank=True)
	posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	

