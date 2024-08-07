from django.shortcuts import render, redirect
from inventory.models import Icategory, ainventory
from datetime import datetime

def add_inventory(request):
    if request.method == 'POST':
        inventory_category_id = request.POST.get('inventory_category')
        shelf_number = request.POST.get('shelf_number')
        purchase_id = request.POST.get('purchase_id')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        expiry_date = request.POST.get('expiry_date')
        price = request.POST.get('price')

    
        if (inventory_category_id and shelf_number and purchase_id and item and
                quantity and unit and expiry_date and price):

            unit_valid = any(unit_choice[0] == unit for unit_choice in ainventory.UNIT_CHOICES)
            if not unit_valid:
                categories = Icategory.objects.all()
                return render(request, 'inventory/add_inventory.html', {
                    'error_message': 'Invalid unit selected.',
                    'categories': categories,
                    'unit_choices': ainventory.UNIT_CHOICES
                })

            # Convert inventory_category_id to Icategory object
            inventory_category = Icategory.objects.get(id=inventory_category_id)

            # Create new ainventory object and save to database
            new_inventory_item = ainventory.objects.create(
                inventory_category=inventory_category,
                shelf_number=shelf_number,
                purchase_id=purchase_id,
                item=item,
                quantity=quantity,
                unit=unit,
                expiry_date=expiry_date,
                price=price
            )
            # Redirect to the add_inventory page upon successful creation
            return redirect('inventory:add_inventory')
        else:

            inventory_items = ainventory.objects.all()
            categories = Icategory.objects.all()
            return render(request, 'inventory/add_inventory.html', {
                'inventory': inventory_items,
                'categories': categories,
                'unit_choices': ainventory.UNIT_CHOICES,
                'error_message': 'All fields are required.'
            })

    inventory_items = ainventory.objects.all()
    categories = Icategory.objects.all()
    return render(request, 'inventory/add_inventory.html', {
        'inventory': inventory_items,
        'categories': categories,
        'unit_choices': ainventory.UNIT_CHOICES
    })

def dinventory(request, id):
    inventory_item = ainventory.objects.get(id=id)
    inventory_item.delete()
    return redirect('inventory:add_inventory')

def uinventory(request, id):
    if request.method == 'POST':
        inventory_category_id = request.POST.get('inventory_category')
        shelf_number = request.POST.get('shelf_number')
        purchase_id = request.POST.get('purchase_id')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        expiry_date = request.POST.get('expiry_date')
        price = request.POST.get('price')
        
        inventory_item = ainventory.objects.get(id=id)
            
        if (inventory_category_id and shelf_number and purchase_id and item and
            quantity and unit and expiry_date and price):
            
            unit_valid = any(unit_choice[0] == unit for unit_choice in ainventory.UNIT_CHOICES)
            if not unit_valid:
                categories = Icategory.objects.all()
                return render(request, 'inventory/edit_inventory.html', {
                    'inventory_item': inventory_item,
                    'categories': categories,
                    'unit_choices': ainventory.UNIT_CHOICES,
                    'error_message': 'Invalid unit selected.'
                })
            
            inventory_category = Icategory.objects.get(id=inventory_category_id)
            inventory_item.inventory_category = inventory_category
            inventory_item.shelf_number = shelf_number
            inventory_item.purchase_id = purchase_id
            inventory_item.item = item
            inventory_item.quantity = quantity
            inventory_item.unit = unit
            inventory_item.expiry_date = expiry_date
            inventory_item.price = price
            inventory_item.save()
            
            
            return redirect('inventory:add_inventory')
        else :
            pass
        
    inventory_item = ainventory.objects.get(pk=id)
    categories = Icategory.objects.all()
    return render(request, 'inventory/edit_inventory.html', {
        'inventory_item': inventory_item,
        'categories': categories,
        'unit_choices': ainventory.UNIT_CHOICES
    })