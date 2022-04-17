from tokenize import Name
from unicodedata import category
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


# Create your models here.
class WorkArt(models.Model):
    #account=models.ForeignKey(account, ondelete=models.CASCADE)
    Name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to=upload_to, null=True, blank=True)
    Externallink=models.URLField(null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Supply=models.IntegerField(null=True,blank=True)
    #BlockChain=models.CharField(max_length=5,null=True,blank=True)
    
class collection(models.Model):
    Logoimage=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    Featuredimage=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    Bannerimage=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    Name=models.CharField(max_length=200,null=True,blank=True)
    URL=models.CharField(max_length=200,null=True,blank=True)
    Description=models.CharField(max_length=900,null=True,blank=True)
    category=models.CharField(max_length=200,null=True,blank=True)
    DisplayTheme=models.CharField(max_length=200,null=True,blank=True)
    WorkArts=models.ManyToManyField(WorkArt,related_name='collections', verbose_name=_('WorkArts'),null=True,blank=True)


class account(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    bio=models.CharField(max_length=500,null=True,blank=True)
    avatar=models.ImageField(upload_to=upload_to, null=True, blank=True)
    banner=models.ImageField(upload_to=upload_to, null=True, blank=True)
    socials=models.URLField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    favorite=models.ManyToManyField(WorkArt,related_name='favorites', verbose_name=_('members'),null=True,blank=True)
    collection=models.ManyToManyField(collection,verbose_name=_('members'),related_name='collections',null=True, blank=True)
    WalletInfo=models.CharField(max_length=500, primary_key=True)
    
    
#class WalletInfo(models.Model):