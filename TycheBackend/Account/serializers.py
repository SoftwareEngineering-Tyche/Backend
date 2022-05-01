from rest_framework import serializers
from .models import account, collection, WorkArt

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ['username','bio','avatar','banner','socials','email','favorite','collection','WalletInfo','WorkArt']
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields = ['id','logoimage','featuredimage','bannerimage','Name','URL','Description','category','DisplayTheme','WorkArts']
class WorkArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkArt
        fields = ['id','Name','image','Externallink','Description','Supply','Description','BlockChain']