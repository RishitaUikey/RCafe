from django.db import models

# Create your models here.
class sorder(models.Model):
    order_id = models.IntegerField()
    food_item = models.CharField( max_length=50)
    quantity = models.IntegerField()
    total = models.IntegerField()
