from django.db import models

# Create your models here.

class category(models.Model):
    name_category = models.CharField(max_length=50)
    
class amenu(models.Model):
    food_category=models.ForeignKey(category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    picture= models.FileField(upload_to='product/',null=True ,blank=True)
    quantity = models.IntegerField()
    
 
