from django.db import models

# Create your models here.
class POS(models.Model):
    DINE_IN = 'dine_in'
    TAKE_OUT = 'take_out'
    DELIVERY = 'delivery'
    
    OPTION_TO_EAT_CHOICES = [
        (DINE_IN, 'Dine In'),
        (TAKE_OUT, 'Take Out'),
        (DELIVERY, 'Delivery'),
    ]
    
    order_date = models.DateField()
    Customer_name = models.CharField( max_length=50)
    Email= models.EmailField(max_length=50,blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    option_to_eat = models.CharField( 
        max_length=50,
        choices=OPTION_TO_EAT_CHOICES,
        default=DINE_IN,
    )
