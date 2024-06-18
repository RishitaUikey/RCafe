from django.db import models
from django.contrib.auth.models import User
from menu.views import amenu
# Create your models here.
class order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at= models.DateTimeField(auto_now_add=True)
    order_id = models.IntegerField()
    food_item = models.CharField( max_length=50)
    quantity = models.IntegerField()
    total = models.FloatField()
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', null=True)
    @property
    def status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status)
    
class orderitem(models.Model):
    order=models.ForeignKey(order, on_delete=models.CASCADE)
    menu_ordered=models.ForeignKey(amenu, on_delete=models.CASCADE, null=True, blank=True)
    quantity=models.IntegerField()
    total_price=models.FloatField(null=True,blank=True)
     
    @property
    def total(self):
        return int(self.menu_ordered.price)*self.quantity 

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_menu=models.ForeignKey(amenu, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    @property
    def total(self):
        return int(self.productorder.price)*self.quantity