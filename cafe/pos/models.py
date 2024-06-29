from django.db import models
from menu.models import amenu
from django.contrib.auth.models import User

# class POS(models.Model):
#     DINE_IN = 'dine_in'
#     TAKE_OUT = 'take_out'
#     DELIVERY = 'delivery'
    
#     OPTION_TO_EAT_CHOICES = [
#         (DINE_IN, 'Dine In'),
#         (TAKE_OUT, 'Take Out'),
#         (DELIVERY, 'Delivery'),
#     ]
    
#     order_date = models.DateField()
#     customer_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     option_to_eat = models.CharField(
#         max_length=10,
#         choices=OPTION_TO_EAT_CHOICES,
#         default=DINE_IN,
#     )
    
#     def __str__(self):
#         return self.customer_name 

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    menu_order = models.ManyToManyField(amenu, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    def __str__(self):
        return str(self.id)
    
    @property
    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuorder = models.ForeignKey(amenu, on_delete=models.CASCADE, related_name='menu_ordered_items')
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(null=True, blank=True)   

    def __str__(self):
        return str(self.order.id)

    @property
    def total(self):
        return int(self.menuorder.price) * self.quantity

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_carts')
    productorder = models.ForeignKey(amenu, on_delete=models.CASCADE, null=True, related_name='menu_carts')
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        return int(self.productorder.price) * self.quantity
