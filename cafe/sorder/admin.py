from django.contrib import admin
from sorder.models import order
# Register your models here.

@admin.register(order) # decorator
class orderAdmin(admin.ModelAdmin):
    list_display=['order_id', 'food_item','quantity', 'total']
