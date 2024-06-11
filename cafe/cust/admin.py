from django.contrib import admin
from cust.models import customer

# Register your models here.
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display= ['name', 'mobile','email', 'address','customer_id', 'created_at']