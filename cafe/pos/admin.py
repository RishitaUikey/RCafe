from django.contrib import admin
from .models import Order,OrderItem

class POSAdmin(admin.ModelAdmin):
    # list_display = ('order_date', 'Customer_name', 'Email', 'Phone', 'Address', 'option_to_eat')
    list_filter = ('order_date', 'option_to_eat')
    search_fields = ('Customer_name', 'Email', 'Phone', 'Address')


