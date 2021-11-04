from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

def index(request):
    return HttpResponse("Hello you're at the calculator app index")

def calculate_tax(price):
    '''
    calculate the tax of a product
    '''
    return price * 1.19


def POST(request):
    """
    Return JSON price + tax.
    """
    return Response({'taxed_price': calculate_tax(request.body.base_price)})

class POSTView(APIView):
    permission_classes = [permissions.AllowAny]

    def POST(request):
        """
        Return JSON price + tax.
        """
        return Response({'taxed_price': calculate_tax(request.body.base_price)})