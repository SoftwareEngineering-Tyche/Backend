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
    account=models.ForeignKey(account, ondelete=models.CASCADE)
    Name=models.CharField(max_length=100)
    image=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    Externallink=models.URLField()
    Description=models.CharField(max_length=200)
    Supply=models.IntegerField()
    BlockChain=models.CharField(max_length=5)
    
class Collection(models.Model):
    Logoimage=models.ImageField()
    Featuredimage=models.ImageField()
    Bannerimage=models.ImageField()
    Name=models.CharField(max_length=200)
    URL=models.CharField(max_length=200)
    Description=models.CharField(max_length=900)
    category=models.CharField(max_length=200)
    DisplayTheme=models.CharField(max_length=200)


class account(models.Model):
    username=models.CharField(max_length=100,null=False)
    bio=models.CharField(max_length=500,null=False)
    avatar=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    banner=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    socials=models.URLField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    favorite=models.ManyToManyField(WorkArt,related_name='favorites', verbose_name=_('members'))
    collection=models.ManyToManyField(Collection,verbose_name=_('members'),related_name='collections')
    WalletInfo=models.CharField(max_length=500,null=True, blank=True)
    
    
#class WalletInfo(models.Model):