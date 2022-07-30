from rest_framework import serializers
from .models import OrderedItem
        
class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'
