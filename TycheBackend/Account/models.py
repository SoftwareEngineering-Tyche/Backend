from tokenize import Name
from unicodedata import category
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import os


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"
class workartoffer(models.Model):
    Price=models.FloatField(null=True, blank=True)
    usdPrice=models.FloatField(null=True, blank=True)
    Date=models.DateTimeField(null=True, blank=True) 
    From=models.CharField(max_length=100,null=True, blank=True) 
    status=models.CharField(max_length=100,default="Pending",null=True, blank=True)   
class property(models.Model):
    subject=models.CharField(max_length=100,null=True,blank=True)
    value=models.CharField(max_length=100,null=True,blank=True)

class statistic(models.Model):
    subject=models.CharField(max_length=100,null=True,blank=True)
    value=models.IntegerField(default=0,null=True,blank=True)

# Create your models here.
    
class workart(models.Model):
    #account=models.ManyToManyField(account,related_name='accounts', verbose_name=_('WorkArts'),null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
    Externallink=models.CharField(max_length=200,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Supply=models.IntegerField(null=True,blank=True)
    Liked=models.IntegerField(default=0,null=True,blank=True)
    BlockChain=models.CharField(default='Ether',max_length=5,null=True,blank=True)
    Price=models.FloatField(null=True,blank=True)
    properties=models.ManyToManyField(property,related_name='properties', null=True,blank=True)
    statistics=models.ManyToManyField(statistic,related_name='statistics', null=True,blank=True)
    WorkArtOffers=models.ManyToManyField(workartoffer,related_name='WorkArtOffers', null=True,blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    
class collection(models.Model):
    logoimage=models.ImageField(_("Logoimage"),upload_to=upload_to, null=True, blank=True)
    featuredimage=models.ImageField(_("Featuredimage"),upload_to=upload_to, null=True, blank=True)
    bannerimage=models.ImageField(_("Bannerimage"),upload_to=upload_to, null=True, blank=True)
    Name=models.CharField(max_length=200,null=True,blank=True)
    URL=models.CharField(max_length=200,null=True,blank=True)
    Description=models.CharField(max_length=900,null=True,blank=True)
    category=models.CharField(max_length=200,null=True,blank=True)
    DisplayTheme=models.CharField(max_length=200,null=True,blank=True)
    WorkArts=models.ManyToManyField(workart,related_name='collections', verbose_name=_('WorkArts'),null=True,blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    Liked=models.IntegerField(default=0,null=True,blank=True)

class account(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    bio=models.CharField(max_length=500,null=True,blank=True)
    avatar=models.ImageField(_("Avatar"),upload_to=upload_to, null=True, blank=True)
    banner=models.ImageField(_("Banner"),upload_to=upload_to, null=True, blank=True)
    socials=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    favorites=models.ManyToManyField(workart,related_name='favorites', verbose_name=_('members'),null=True,blank=True)
    collections=models.ManyToManyField(collection,verbose_name=_('members'),related_name='collections',null=True, blank=True)
    WalletInfo=models.CharField(max_length=500, primary_key=True)
    WorkArts=models.ManyToManyField(workart,verbose_name=_('accounts'),related_name='WorkArts',null=True, blank=True)
    WorkArtOffers=models.ManyToManyField(workartoffer,verbose_name=_('wfaccounts'),related_name='workartoffers',null=True, blank=True)