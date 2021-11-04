from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('POST/', views.POST, name='calculator'),
]