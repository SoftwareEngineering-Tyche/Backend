from rest_framework import serializers
from .models import account, collection, WorkArt

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ['username','bio','avatar','banner','socials','favorite','collection','WalletInfo']
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields = ['Logoimage','Featuredimage','Bannerimage','Name','URL','Description','category','DisplayTheme','WorkArts']
class WorkArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkArt
        fields = ['Name','image','Externallink','Description','Supply','Description','BlockChain']