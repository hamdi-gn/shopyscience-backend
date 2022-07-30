from rest_framework import serializers
from .models import Conact

        
class ConactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conact
        fields = '__all__'
