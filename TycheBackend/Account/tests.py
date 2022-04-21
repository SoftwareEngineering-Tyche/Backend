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
        url = 'http://127.0.0.1:8000/account/'
        data = {'Name': 'hasan.sabour.iust@gmail.com',
                'Description':'hasan'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(response.data, data)
        #self.assertIsInstance(Account,account)