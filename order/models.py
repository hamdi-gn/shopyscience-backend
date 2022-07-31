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