import collections
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import account , collection, workart, statistic, property, workartoffer
from .serializers import AccountSerializer, CollectionSerializer, WorkArtSerializer, PropertySerializer, StatisticSerializer, WorkArtOfferSerializer
from rest_framework.parsers import MultiPartParser,FormParser
import json
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
# Create your views here.
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

def validate_data(data, required_data):
    for key in required_data:
        if key not in data:
            return False
    return True


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
    def post(self,request,pk):
        parser_classes=[MultiPartParser, FormParser]
        serializer=WorkArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            MyWorkArt=workart.objects.get(id=serializer.data['id'])           
            query=collection.objects.get(id=pk)
            query.WorkArts.add(MyWorkArt)
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
class WorkArtLike(APIView):
    def get (self,request,pk):
        a=workart.objects.get(id=pk)
        MyAccount=account.objects.get(WalletInfo=request.data['WalletInfo'])
        list=MyAccount.favorites.all()
        isliked=list.filter(id=a.id).exists()
        return Response(isliked,status.HTTP_200_OK) 
            
    def post(self,request,pk):
        parser_classes=[MultiPartParser, FormParser]
        a=workart.objects.get(id=pk)
        MyAccount=account.objects.get(WalletInfo=request.data['WalletInfo'])
        list=MyAccount.favorites.all()
        isliked=list.filter(id=a.id).exists()
        if isliked:
            MyAccount.favorites.remove(a)
            a.Liked-=1
        else:
            MyAccount.favorites.add(a)
            a.Liked+=1
        
        a.save()
        s=str(a.Liked)
        return Response(s, status=status.HTTP_200_OK)
   
class WorkArtLiked(APIView):
    def post (self,request,pk):
        a=workart.objects.get(id=pk)
        MyAccount=account.objects.get(WalletInfo=request.data['WalletInfo'])
        list=MyAccount.favorites.all()
        isliked=list.filter(id=a.id).exists()
        return Response(isliked,status.HTTP_200_OK) 
class WorkArtProperty(APIView):
    def get(self,request,pk):
        myworkart=workart.objects.get(id=pk)
        myp=myworkart.properties.all()
        serializer=PropertySerializer(myp,many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request,pk):
        serializer=PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a=property.objects.get(subject=serializer.data['subject'])
            MyWorkArt=workart.objects.get(id=pk)
            MyWorkArt.properties.add(a)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
      
    
class WorkArtstatistic(APIView):
    def get(self,request,pk):
        myworkart=workart.objects.get(id=pk)
        myp=myworkart.statistics.all()
        serializer=StatisticSerializer(myp,many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request,pk):
        serializer=StatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a=statistic.objects.get(subject=serializer.data['subject'])
            MyWorkArt=workart.objects.get(id=pk)
            MyWorkArt.statistics.add(a)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)      

class WorkArtCollection(APIView):
    def get(self, request,pk):
        a=workart.objects.get(id=pk)
        s=a.collections.all()
        query=collection.objects.get(id=s[0].id)
        l=query.WorkArts.all()
        d=WorkArtSerializer(l,many=True)
        return Response(d.data, status=status.HTTP_200_OK)
class collectionworkarts(APIView):
    def get(self, request,pk):
        mycollection=collection.objects.get(id=pk)
        myworkarts=mycollection.WorkArts.all()
        d=WorkArtSerializer(myworkarts,many=True)
        return Response(d.data,status.HTTP_200_OK)
        
class AccountWorkarts(APIView):
    def get(self, request,pk):
        query=account.objects.get(WalletInfo=pk)
        l=query.collections.all()
        list=[]
        for i in l:
            o=i.WorkArts.all()
            for z in o:
                list.append(z)
        serializer=WorkArtSerializer(list,many=True)
        print(str(list[0]))
        return Response(serializer.data,status.HTTP_200_OK)

#favorites

class Accountfavorites(APIView):
    def get(self, request,pk):
        query=account.objects.get(WalletInfo=pk)
        query=query.favorites.all()
        serializer=WorkArtSerializer(query,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
class Search(APIView):
    def get(self, req):
        data = req.data
        # check data
        if not validate_data(data, ['search']):
            return Response({'status':'failed', 'data':{}, 'message':f"required_data: {['search']}"}, status=400)
        serachfield = data["search"]


        #accounts
        userfilter=(Q(username__contains=serachfield)| Q(email__contains=serachfield)|Q(bio__contains=serachfield)|Q(socials__contains=serachfield) | Q(WalletInfo__contains=serachfield))
        res=account.objects.complex_filter(userfilter)
        users=AccountSerializer(res,many=True)


        #NFTs
        nftfilter=(Q(Name__contains=serachfield)| Q(Externallink__contains=serachfield)|Q(Description__contains=serachfield))
        res=workart.objects.complex_filter(nftfilter)
        nfts=WorkArtSerializer(res,many=True)

        #collections
        collectionsfilter=(Q(Name__contains=serachfield)| Q(URL__contains=serachfield)|Q(Description__contains=serachfield)| Q(category__contains=serachfield))
        res=collection.objects.complex_filter(collectionsfilter)
        collections=CollectionSerializer(res,many=True)

        #property
        propertyfilter=(Q(keyId__contains=serachfield)| Q(value__contains=serachfield))
        res=property.objects.complex_filter(propertyfilter)
        properties=PropertySerializer(res,many=True)


        #statistic
        statisticfilter=(Q(keyId__contains=serachfield)| Q(value__contains=serachfield))
        res=statistic.objects.complex_filter(statisticfilter)
        statistics=StatisticSerializer(res,many=True)



        return Response({'status':'success', 'data':{'accounts':users.data, 'NFTs':nfts.data, 'collections':collections.data, 'properties':properties.data, 'statistics':statistics.data}, 'message':''},status=200)



class Explore(APIView):
    def post(self, request):
        data = request.data
        # check data
        if not validate_data(data, ['hotest','favorites','latest']):
            return Response({'status':'failed', 'data':{}, 'message':f"required_data: {['hotest','favorites','latest']}"}, status=400)

        result={'hotest':[],'favorites':[],'latest':[]}
        res=collection.objects.all()
        n= len(res)
        if data['hotest']:
            hotest=CollectionSerializer(res[(2*n)//3:],many=True)
            result['hotest'].append(hotest.data)

        if data['favorites']:
            favorites=CollectionSerializer(res[n//3:(2*n)//3],many=True)
            result['favorites'].append(favorites.data)


        if data['latest']:
            latest=CollectionSerializer(res[:n//3],many=True)
            result['latest'].append(latest.data)


        return Response({'status':'success', 'data':result, 'message':''},status=200)


class SortNFT(APIView):
    def get(self, req):
        data = req.data
        # check data

        if not validate_data(data, ['params','kind']):
            return Response({'status':'failed', 'data':{}, 'message':f"required_data: {['params','kind']}"}, status=400)
        res=[]
        NFTS=workart.objects.all()

        if data['params']=='price':
            res = NFTS.order_by('Price')

        elif data['params']=='liked':
            res = NFTS.order_by('Liked')

        elif data['params']=='date':
            res = NFTS.order_by('created_at')
        else :
            return Response({'status':'failed', 'data':{}, 'message':f"wrong params for sorting"}, status=400)




        d=WorkArtSerializer(res,many=True)
        if data['kind']=='ascending':
            return Response({'status':'success', 'data':d.data, 'message':''},status=200)

        elif data['kind']=='descending':
            q=WorkArtSerializer(res.reverse(),many=True)

            return Response({'status':'success', 'data':q.data, 'message':''},status=200)
        else :
            return Response({'status':'failed', 'data':{}, 'message':f"wrong sort kind "}, status=400)


class Sortcollection(APIView):
    def get(self, req):
        data = req.data
        # check data

        if not validate_data(data, ['params','kind']):
            return Response({'status':'failed', 'data':{}, 'message':f"required_data: {['params','kind']}"}, status=400)
        res=[]

        collections=collection.objects.all()

        if data['params']=='liked':
            res = collections.order_by('Liked')

        elif data['params']=='date':
            res = collections.order_by('created_at')
        else :
            return Response({'status':'failed', 'data':{}, 'message':f"wrong params for sorting"}, status=400)


        d=CollectionSerializer(res,many=True)
        if data['kind']=='ascending':
            return Response({'status':'success', 'data':d.data, 'message':''},status=200)

        elif data['kind']=='descending':
            q=CollectionSerializer(res.reverse(),many=True)
            return Response({'status':'success', 'data':q.data, 'message':''},status=200)
        else :
            return Response({'status':'failed', 'data':{}, 'message':f"wrong sort kind "}, status=400)

class WorkArtOffer(APIView):
    def post(self,request,pk):
        accountid=account.objects.get(WalletInfo=request.data['From'])
        serializer=WorkArtOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            workartofferid=workartoffer.objects.get(id=serializer.data['id'])
            mynow=timezone.now()
            k=gregorian_to_jalali(mynow.year,mynow.month,mynow.day) 
            now=datetime.now() 
            now=datetime(k[0],k[1],k[2],mynow.hour,mynow.minute,mynow.second,0)
            workartofferid.Date=now
            workartofferid.save()
            workartl=workart.objects.get(id=pk)
            workartl.WorkArtOffers.add(workartofferid)
            accountid.WorkArtOffers.add(workartofferid)
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)   
    def get(self,request,pk):
        workartid=workart.objects.get(id=pk)
        workartoffers=workartid.WorkArtOffers.all()
        serializer=WorkArtOfferSerializer(workartoffers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class accountworkarts(APIView):
    def get(self,request,pk):
        accountid=accountworkarts.objects.get(WalletInfo=pk)
        workartoffers=accountid.WorkArtOffers.all()
        serializer=WorkArtOfferSerializer(data=workartoffers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
class  worrkartofferaccept(APIView):
    def post(self,request,pk):
        workartid=workartoffer.objects.get(id=pk)
        if request.data["status"]=="accepted":
            workartid.status="accepted"
        else:
            workartid.status="rejected"
        workartid.save()
        return Response("Ok",status=status.HTTP_200_OK)
             