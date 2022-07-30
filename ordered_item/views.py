from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import OrderedItemSerializer, OrderedItem
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class OrderedItemViewSet(viewsets.ModelViewSet):    
    queryset = OrderedItem.objects.all()
    serializer_class = OrderedItemSerializer
    permission_classes = [IsAuthenticated]
    
