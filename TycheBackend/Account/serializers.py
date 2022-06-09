from rest_framework import serializers
from .models import account, collection, workart, property, statistic, WorkArtOffer

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields = ['id','logoimage','featuredimage','bannerimage','Name','URL','Description','category','DisplayTheme','WorkArts','created_at']
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
        model=WorkArtOffer
        fields=['Price','usdPrice','Date']