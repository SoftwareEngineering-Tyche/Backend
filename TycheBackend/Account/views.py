from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import account , collection, WorkArt
from .serializers import AccountSerializer, CollectionSerializer, WorkArtSerializer
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.


class Account(APIView):
    def post(self,request):
        parser_classes=[MultiPartParser, FormParser]
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #query=account()
        #query.WalletInfo=request.data['WalletInfo']
        #query.username=request.data['username']
        #query.avatar=request.data['avatar']
        #query.WalletInfo=request.data['WalletInfo']
        #query.banner=request.data['banner']
        #query.bio=request.data['bio']
        #query.email=request.data['email']
        #query.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    def put(self,request,format=None):
        parser_classes=(MultiPartParser, FormParser)
        try:
            query=account.objects.get(WalletInfo=request.data.get('WalletInfo'))
        except:
            return Response("Error",status.HTTP_200_OK)
        #serializer=AccountSerializer(data=request.data)
        #if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status.HTTP_200_OK)
        query.username=request.data['username']
        query.avatar=request.data['avatar']
        query.WalletInfo=request.data['WalletInfo']
        query.banner=request.data['banner']
        query.bio=request.data['bio']
        query.email=request.data['email']
        query.save()
        return Response(request.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        serializer=AccountSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
    def delete(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        serializer=AccountSerializer(query)
        query.delete()
        return Response(serializer.data,status.HTTP_200_OK)

class collectionView(APIView):
    def post(self,request):
        parser_classes=[MultiPartParser, FormParser]
        #serializer=CollectionSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        query=collection()
        query.Logoimage=request.data['Logoimage']
        query.Featuredimage=request.data['Featuredimage']
        query.Bannerimage=request.data['Bannerimage']
        query.Name=request.data['Name']
        query.URL=request.data['URL']
        query.Description=request.data['Description']
        query.category=request.data['category']
        query.DisplayTheme=request.data['DisplayTheme']
        query.WorkArts=request.data['WorkArts']
        query.save()
        
        return Response(request.data, status=status.HTTP_201_CREATED)
    def put(self,request,pk):
        parser_classes=[MultiPartParser, FormParser]
        try:
            query=collection.objects.get(id=pk)
        except:
            return Response("Error",status.HTTP_400_BAD_REQUEST)
        query.Logoimage=request.data['Logoimage']
        query.Featuredimage=request.data['Featuredimage']
        query.Bannerimage=request.data['Bannerimage']
        query.Name=request.data['Name']
        query.URL=request.data['URL']
        query.Description=request.data['Description']
        query.category=request.data['category']
        query.DisplayTheme=request.data['DisplayTheme']
        query.WorkArts=request.data['WorkArts']
        query.save()
        serializer=CollectionSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(query.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=collection.objects.get(id=pk)
        serializer=CollectionSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
class WorkArt(APIView):
    def post(self,request):
        parser_classes=[MultiPartParser, FormParser]
        #serializer=WorkArtSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        query=WorkArt()
        query.Name=request.data['Name']
        query.image=request.data['image']
        query.Externallink=request.data['Externallink']
        query.Description=request.data['Description']
        query.Supply=request.data['Supply']
        query.Liked=request.data['Liked']
        query.save()
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        parser_classes=[MultiPartParser, FormParser]
        try:
            query=WorkArt.objects.get(id=pk)
        except:
            return Response("Error",status.HTTP_400_BAD_REQUEST)
        #serializer=WorkArtSerializer(query,data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data,status.HTTP_200_OK)
        query=WorkArt()
        query.Name=request.data['Name']
        query.image=request.data['image']
        query.Externallink=request.data['Externallink']
        query.Description=request.data['Description']
        query.Supply=request.data['Supply']
        query.Liked=request.data['Liked']
        query.save()
        return Response(request.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=WorkArt.objects.get(id=pk)
        serializer=WorkArtSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
    
        
    

            