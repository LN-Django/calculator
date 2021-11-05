from rest_framework import routers
from .api.ping import PingView
from .api.products import ProductViewSet
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, 'products')

urlpatterns = [
    url('api/ping', PingView.as_view()),
]

urlpatterns += router.urls
