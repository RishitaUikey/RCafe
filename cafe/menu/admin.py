from django.contrib import admin
from menu.models import amenu,category
# Register your models here.

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display =['name_category']
@admin.register(amenu) # decorator
class amenuAdmin(admin.ModelAdmin):
    list_display=['food_category', 'name','price', 'quantity']

