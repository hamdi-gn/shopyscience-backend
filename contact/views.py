from django.shortcuts import render
from .serializers import Conact, ConactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ConactViewSet(viewsets.ModelViewSet):    
    queryset = Conact.objects.all()
    serializer_class = ConactSerializer
    permission_classes = [IsAuthenticated]