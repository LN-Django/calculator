from rest_framework import routers
from .api.ping import PingView
from .api.products import ProductViewSet
from django.conf.urls import url
from django.urls import path, include
from calculator.views import POSTView


router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, 'products')

urlpatterns = [
    url('api/ping', PingView.as_view()),
    path('calculator/', include('calculator.urls')),
    url('calculator/POST/', POSTView.as_view() )
    #path('calculator/POST/', include('calculator.urls')),
]

urlpatterns += router.urls
