from rest_framework import serializers
from .models import account, collection, workart

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
        fields = ['username','bio','avatar','collections','banner','socials','email','favorite','WalletInfo','WorkArt']

class WorkArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=workart
        fields = ['id','Price','Name','image','Externallink','Description','Supply','Description','BlockChain']
