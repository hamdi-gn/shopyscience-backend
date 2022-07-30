from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Conact(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AccountName = models.CharField(max_length=50)
    AddressLine1 = models.CharField(max_length=50)
    AddressLine2 = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50)
    ContactName = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    ZipCode = models.IntegerField()
    

    def __str__(self):
       return "%s" % (self.AccountName)
    class Meta:
        ordering = ['AccountName']

