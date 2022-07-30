from django.shortcuts import render
from .serializers import Item, ItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]