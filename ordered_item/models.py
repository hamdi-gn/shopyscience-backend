from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class OrderedItem(models.Model):
    Amount = models.FloatField()
    Description = models.CharField(max_length=255)  
    Discount = models.FloatField()
    Item = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    ItemDescription = models.CharField(max_length=255)  
    Quantity = models.IntegerField()
    UnitCode = models.CharField(max_length=50)
    UnitDescription = models.CharField(max_length=50)
    UnitPrice = models.FloatField()
    VATAmount = models.FloatField()
    VATPercentage = models.FloatField()
    

    def __unicode__(self):
        return self.Item
