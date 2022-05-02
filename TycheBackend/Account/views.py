from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import account , collection, workart
from .serializers import AccountSerializer, CollectionSerializer, WorkArtSerializer
from rest_framework.parsers import MultiPartParser,FormParser
import json
# Create your views here.


class Account(APIView):
    def post(self,request):
        parser_classes=[MultiPartParser, FormParser]
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_201_CREATED)
    def put(self,request,format=None):
        parser_classes=(MultiPartParser, FormParser)
        try:
            query=account.objects.get(WalletInfo=request.data.get('WalletInfo'))
        except:
            return Response("Error",status.HTTP_200_OK)
        serializer=AccountSerializer(query,data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status.HTTP_200_OK)
        return Response(request.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        #a=collection.objects.get()
        #l=query.collections.all()
        #d=CollectionSerializer(l,many=True)
        serializer=AccountSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
    def delete(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        serializer=AccountSerializer(query)
        query.delete()
        return Response(serializer.data,status.HTTP_200_OK)

class AccountCollection(APIView):
    def get(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        #a=collection.objects.get()
        l=query.collections.all()
        d=CollectionSerializer(l,many=True)
        return Response(d.data,status.HTTP_200_OK)

class collectionView(APIView):
    def post(self,request,pk,format=None):
        parser_classes=[MultiPartParser, FormParser]
        serializer=CollectionSerializer(data=request.data)
        query=account.objects.get(WalletInfo=pk)
        if serializer.is_valid():
            serializer.save()
            mycollection=collection.objects.get(id=serializer.data['id'])
            query.collections.add(mycollection)
            query.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_201_CREATED)
    def put(self,request,pk,format=None):
        parser_classes=[MultiPartParser, FormParser]
        try:
            query=collection.objects.get(id=pk)
        except:
            return Response("Error",status.HTTP_400_BAD_REQUEST)
        serializer=CollectionSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(query.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=collection.objects.get(id=pk)
        serializer=CollectionSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
    def delete(self,request,pk):
        query=account.objects.get(WalletInfo=pk)
        serializer=AccountSerializer(query)
        query.delete()
        return Response(serializer.data,status.HTTP_200_OK)
class WorkArt(APIView):
    def post(self,request):
        parser_classes=[MultiPartParser, FormParser]
        serializer=WorkArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        parser_classes=[MultiPartParser, FormParser]
        try:
            query=workart.objects.get(id=pk)
        except:
            return Response("Error",status.HTTP_400_BAD_REQUEST)
        serializer=WorkArtSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(request.data,status.HTTP_200_OK)
    def get(self,request,pk):
        query=workart.objects.get(id=pk)
        serializer=WorkArtSerializer(query)
        return Response(serializer.data,status.HTTP_200_OK)
    def delete(self,request,pk):
        query=workart.objects.get(id=pk)
        serializer=WorkArtSerializer(query)
        query.delete()
        return Response(serializer.data,status.HTTP_200_OK)
        
    

            