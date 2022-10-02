from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getDataSize', views.getDataSize, name='getDataSize'),
    path('testBubbleSort', views.testBubbleSort, name='testBubbleSort')
]