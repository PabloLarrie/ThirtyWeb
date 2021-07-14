from django.db import models


class Post(models.Model):
    tittle = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, null=True)
    image = models.ImageField(required=True)
    hashtags = models.TextField(max_length=300, null=True)
    