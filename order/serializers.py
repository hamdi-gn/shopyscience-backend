from dataclasses import fields
from pickle import FALSE
from rest_framework import serializers
from .models import Order
from ordered_item.serializers import OrderedItemSerializer
from contact.serializers import ConactSerializer

        
class OrderSerializer(serializers.ModelSerializer):
    SalesOrderLines = OrderedItemSerializer(source='orders_data',many=True, read_only=True)
    Conact_Name = ConactSerializer(source='DeliverTo',many=False, read_only=True)
    class Meta:
        model = Order
        fields = ('Amount', 'Currency', 'DeliverTo', 'Conact_Name', 'OrderID', 'OrderNumber', 'SalesOrderLines', 'orders_data')

""" class OrderCSVSerializer(serializers.ModelSerializer):
    itemindex = OrderedItemSerializer(source='item_index',many=True, read_only=True)
    itemid = OrderedItemSerializer(source='item_id',many=True, read_only=True)
    itemquantity = OrderedItemSerializer(source='item_quantity',many=False, read_only=True)
    class Meta:
        model = OrderCSV
        fields = ('itemindex', 'itemid', 'itemquantity', 'order', 'delivery_name', 'delivery_address', 'delivery_country', 'delivery_zipcode', 'delivery_city', 'items_count', 'item_index', 'item_id', 'item_quantity', 'line_price_excl_vat', 'line_price_incl_vat')
 """