from django.db import models

# Create your models here.
class Purchase(models.Model):
    category = models.CharField(max_length=50)
    item = models.CharField(max_length=10,null=True,blank=True)
    unit = models.CharField(max_length=10)
    quantity = models.FloatField(null=True,blank=True)
    entry_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    price =  models.FloatField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    