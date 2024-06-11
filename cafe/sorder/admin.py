from django.contrib import admin
from sorder.models import sorder
# Register your models here.

@admin.register(sorder) # decorator
class sorderAdmin(admin.ModelAdmin):
    list_display=['order_id', 'food_item','quantity', 'total']
