from django.contrib import admin
from inventory.models import inventory,Icategory
# Register your models here.
@admin.register(inventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display=['inventory_category','shelf_number','purchase_id','item','quantity','unit','expiry_date','entry_date','price']
    
@admin.register(Icategory)
class Inventory_categoryAdmin(admin.ModelAdmin):
    list_display =['category_name']