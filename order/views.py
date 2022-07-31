from django.shortcuts import render
from .serializers import Order, OrderSerializer
from ordered_item.models import OrderedItem
from rest_framework import viewsets
from django.http import HttpResponse
import csv
from django.db.models import Sum, Count
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
 
    
    
def export(response):
    
    response = HttpResponse(content_type='text/csv')   
     
    writer = csv.writer(response)
    
    orders = Order.objects.all()
    
    writer.writerow(['order', 'delivery_name', 'delivery_address', 'delivery_country', 'delivery_zipcode', 'delivery_city', 'items_count', 'item_index', 'item_id', 'item_quantity', 'line_price_excl_vat', 'line_price_incl_vat'])
    
    for order in orders:
        writer.writerow([order.OrderNumber, order.DeliverTo.ContactName, order.DeliverTo.AddressLine1, order.DeliverTo.Country, order.DeliverTo.ZipCode, 0, 0, 0, 0, 0, 0])
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    return response