from rest_framework import serializers
from .models import account, collection, workart, property, statistic, workartoffer
from django.utils import timezone
from datetime import datetime

def gregorian_to_jalali(gy, gm, gd):
 g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
 if (gm > 2):
  gy2 = gy + 1
 else:
  gy2 = gy
 days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
 jy = -1595 + (33 * (days // 12053))
 days %= 12053
 jy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  jy += (days - 1) // 365
  days = (days - 1) % 365
 if (days < 186):
  jm = 1 + (days // 31)
  jd = 1 + (days % 31)
 else:
  jm = 7 + ((days - 186) // 30)
  jd = 1 + ((days - 186) % 30)
 return [jy, jm, jd]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields = ['id','logoimage','featuredimage','bannerimage','Name','URL','Description','category','DisplayTheme','WorkArts']
class AccountGETSerializer(serializers.ModelSerializer):
    collections=CollectionSerializer(read_only=True,many=True)
    class Meta:   
        model = account
        fields = '__all__'
class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = account
        fields = ['username','bio','avatar','collections','banner','socials','email','favorites','WalletInfo','WorkArts']

class WorkArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=workart
        fields = ['id','Name','image','Externallink','Liked','Description','Supply','BlockChain','Price','collections','WorkArtOffers']

class PropertySerializer(serializers.ModelSerializer):
        class Meta:
            model=property
            fields = ['subject','value']

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
            model=statistic
            fields = ['subject','value']

class WorkArtOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=workartoffer
        fields=['id','Price','usdPrice','Date','status','From']

        def create(self, validated_data):
            # as long as the fields are the same, we can just use this
            mynow=timezone.now()
            k=gregorian_to_jalali(mynow.year,mynow.month,mynow.day) 
            now=datetime.now() 
            now=datetime(k[0],k[1],k[2],mynow.hour,mynow.minute,mynow.second,0)
            instance = self.Meta.model(**validated_data)
            instance.Date=now
            instance.save()
            return instance