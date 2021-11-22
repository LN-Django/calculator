'''
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from views import POSTView

class CalculatorTest(APITestCase):
    def test_calculator(self):
        """
        Ensure we get response the taxed price.
        """

        client = APIClient
        response = client.get('http://testserver/homepage/')
        #data = {'taxed_price': 'DabApps'}
        response = self.client.post()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''        
