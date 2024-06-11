from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)