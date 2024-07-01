from django.db import models

class Icategory(models.Model):
    category_name = models.CharField(max_length=50, null=True, blank=True)

class ainventory(models.Model):
    LITRES = 'L'
    MILLILITRES = 'mL'
    GRAMS = 'g'
    KILOGRAMS = 'kg'
    PACKETS = 'packets'

    UNIT_CHOICES = [
        (LITRES, 'Litres (L)'),
        (MILLILITRES, 'Millilitres (mL)'),
        (GRAMS, 'Grams (g)'),
        (KILOGRAMS, 'Kilograms (kg)'),
        (PACKETS, 'Packets'),
    ]

    inventory_category = models.ForeignKey(Icategory, on_delete=models.CASCADE, null=True, blank=True)
    shelf_number = models.IntegerField()
    purchase_id = models.IntegerField()
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    expiry_date = models.DateTimeField(null=True)
    entry_date = models.DateField(auto_now_add=True,null=True)
    price = models.IntegerField()
