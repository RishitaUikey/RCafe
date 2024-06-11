from django.contrib import admin
from menu.models import menu,category
# Register your models here.

@admin.register(menu) # decorator
class menuAdmin(admin.ModelAdmin):
    list_display=['food_category', 'name','price', 'quantity']

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display =['name_category']