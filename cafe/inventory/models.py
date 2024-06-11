from django.db import models

# Create your models here.
class inventory(models.Model):
    inventory_category = models.ForeignKey('Icategory',on_delete=models.CASCADE,null=True,blank=True)
    shelf_number = models.IntegerField()
    purchase_id = models.IntegerField()
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.IntegerField()
    expiry_date = models.DateTimeField()
    entry_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    
class Icategory(models.Model):
    category_name = models.CharField(max_length=50,null=True,blank=True)
    