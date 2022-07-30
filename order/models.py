from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from ordered_item.models import OrderedItem
from contact.models import Conact

# Create your models here.
class Order(models.Model):
    Amount = models.FloatField()
    Currency = models.CharField(max_length=50)  
    DeliverTo = models.ForeignKey(Conact, related_name="Conact_Name", on_delete=models.CASCADE)
    OrderID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    OrderNumber = models.IntegerField()
    orders_data = models.ManyToManyField(OrderedItem, related_name="SalesOrderLines", db_constraint=True)

    

    def __unicode__(self):
        return self.OrderID

""" class OrderCSV(models.Model):
    order = models.IntegerField()
    delivery_name = models.CharField(max_length=50)  
    delivery_address = models.CharField(max_length=50)  
    delivery_country = models.CharField(max_length=50)  
    delivery_zipcode = models.IntegerField()  
    delivery_city = models.CharField(max_length=50)  
    items_count = models.IntegerField()  
    item_index = models.ManyToManyField(OrderedItem, related_name="itemindex", db_constraint=True) 
    item_id = models.ManyToManyField(OrderedItem, related_name="itemid", db_constraint=True) 
    item_quantity = models.ManyToManyField(OrderedItem, related_name="itemquantity", db_constraint=True) 
    line_price_excl_vat = models.FloatField()  
    line_price_incl_vat = models.FloatField()  


    def __unicode__(self):
        return self.order """
