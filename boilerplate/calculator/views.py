from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import logging    



def calculate_tax(price):
    '''
    calculate the tax of a product
    '''
    return price * 1.19

class POSTView(APIView):
    
    logger = logging.getLogger('mainLogger')
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'base_price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Base price of a product'),
        }
    ), responses={
        '200': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'taxed_price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Price of the product incl. tax')
            })
    }
    )

    def post(self, request):
        """
        Return JSON price + tax.
        """
        data = request.data

        #Validator
        if (not(data['base_price'].isnumeric()) or data['base_price'] <= 0):
            self.logger.error('Invalid base price!')
            return Response({'message': 'Bad request: invalid parameter'}, status=400)

        return Response({'taxed_price': calculate_tax(data['base_price'])})