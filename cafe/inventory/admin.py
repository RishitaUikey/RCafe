from django.contrib import admin
from inventory.models import ainventory,Icategory
# Register your models here.

@admin.register(Icategory)
class Inventory_categoryAdmin(admin.ModelAdmin):
    list_display =['category_name']
@admin.register(ainventory)
class ainventoryAdmin(admin.ModelAdmin):
    list_display=['inventory_category','shelf_number','purchase_id','item','quantity','unit','expiry_date','entry_date','price']
    
