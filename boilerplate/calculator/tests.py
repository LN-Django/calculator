from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.utils import json

client = APIClient()

class PostCalculatorTest(TestCase):
    def setUp(self) -> None:
        self.base_params = {
            'base_price': 4.0
        }
        return super().setUp()


    def test_post_taxed_price_valid_parameter(self):
        """It should return the status code 200 if the parameter passed is valid"""
        response = client.post(
            reverse('post'),
            data=json.dumps(self.base_params),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)       

    def test_post_taxed_price_invalid_parameter1(self):
        """It should return the status code 400 if the parameter passed is invalid"""
        parameter = self.base_params.copy()
        parameter['base_price'] = -5000

        response = client.post(
            reverse('post'),
            data=json.dumps(parameter),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_post_taxed_price_invalid_parameter2(self):
        """It should return the status code 400 if the parameter passed is invalid"""
        parameter = self.base_params.copy()
        parameter['base_price'] = "hallooooo"

        response = client.post(
            reverse('post'),
            data=json.dumps(parameter),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)      