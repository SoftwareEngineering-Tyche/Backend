from rest_framework.test import APITestCase
#from django.core.urlresolvers import reverse
from rest_framework import status
from .models import account
# Create your tests here.
class AccountTestCase(APITestCase):
    def test_create_account(self):
        Account = account()
        Account.username = 'Hasan'
        Account.email = 'Hasan@gmail.com'
        Account.WalletInfo="dvvdfivkl"
        #account.objects.create('Accfdsfnt','fdsfsdf',null=True,null=True,null=True,null=True,null=True,null=True,'sdfsfscsdjkv')
        url = 'http://127.0.0.1:8000/Account/'
        data = {'WalletInfo': 'hasan.sabour.iust@gmail.com',
                'username':'hasan',
                'avatar':'',
                'banner':'', 
                'bio':'dfsfs',
                'email':'dfsdfs@sdfsd.com'}
        response = self.client.post(url, data,'multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), data.get('username'))
        self.assertEqual(response.data.get('WalletInfo'), data.get('WalletInfo'))
        #self.assertIsInstance(Account,account)