from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class ArticlesUser(AbstractUser):
    email = models.EmailField(unique = True)

class Infofile(models.Model):
    info = models.TextField(blank = True)
    user = models.OneToOneField(ArticlesUser, on_delete= models.CASCADE)

# @receiver(post_save, sender = ArticlesUser)
# def create_info(sender, instance, **kwargs):
#     Infofile.objects.create(user = instance, info = 'some info')
