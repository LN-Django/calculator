from django.conf.urls import url
from . import views

urlpatterns = [
    url('api/calculator', views.POSTView.as_view() )
]