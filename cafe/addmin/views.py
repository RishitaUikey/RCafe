from django.shortcuts import render,redirect
from inventory.models import Icategory,ainventory
from menu.models import amenu,category
from datetime import datetime

def add_inventory(request):
    if request.method == 'POST':
        inventory_category_id = request.POST.get('inventory_category')
        shelf_number = request.POST.get('shelf_number')
        purchase_id = request.POST.get('purchase_id')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        expiry_date_str = request.POST.get('expiry_date')
        price = request.POST.get('price')

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
            return redirect('add_inventory')
        else:
            # If form is incomplete, render the form again with error message
            inventory_items = ainventory.objects.all()
            categories = Icategory.objects.all()
            return render(request, 'inventory/add_inventory.html', {
                'inventory': inventory_items,
                'categories': categories,
                'unit_choices': ainventory.UNIT_CHOICES,
                'error_message': 'All fields are required.'
            })

    # If GET request, render the initial form
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
    return redirect('inventory/add_inventory')

def uinventory(request, id):
    if request.method == 'POST':
        inventory_category_id = request.POST.get('inventory_category')
        shelf_number = request.POST.get('shelf_number')
        purchase_id = request.POST.get('purchase_id')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        expiry_date_s = request.POST.get('expiry_date')
        price = request.POST.get('price')
        
        inventory_item = ainventory.objects.get(id=id)
        
        try:
            expiry_date = datetime.strptime(expiry_date_s, "%Y-%m-%d").date()
        except ValueError:
            categories = Icategory.objects.all()
            return render(request, 'inventory/edit_inventory.html', {
                'inventory_item': inventory_item,
                'categories': categories,
                'unit_choices': ainventory.UNIT_CHOICES,
                'error_message': 'Invalid expiry date format. Please use YYYY-MM-DD.'
            })
            
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
            
            
            return redirect('inventory/add')
        else :
            pass
        
    inventory_item = ainventory.objects.get(pk=id)
    categories = Icategory.objects.all()
    return render(request, 'inventory/edit_inventory.html', {
        'inventory_item': inventory_item,
        'categories': categories,
        'unit_choices': ainventory.UNIT_CHOICES
    })
# Create your views here.

def add_dashboard(request):
    return render(request,'addmin/dashboard.html')

def add_inventory(request):
    return render('inventory/add_inventory')

def dinventory(request, id):
    return render('inventory/add_inventory')

def uinventory(request, id):
    return render('inventory/edit_inventory')

def menuu(request):
    return render(request, 'customer/menu.html')

def addmenu(request):
    return render(request, 'menu/addmenu.html')

def delmenu(request,id):
    return redirect('menu/addmenu')

def upmenu(request,id):
    return render('menu/edit_menu')

def add_purchase(request):
    return render(request, 'purchase/add_purchase.html')  

def dpurchase(request, id):
    return redirect('purchase/add_purchase')

def upurchase(request, id):
    return redirect('purchase/edit_purchase')

def add_cust(request):
    return redirect('pos/add_cust')

def del_cust(request, id):
    return redirect('pos/add_cust')

def up_cust(request, id):
    return render(request, 'pos/edit_cust.html')

def show_orders(request):
        return render(request, 'pos/cart.html')


    
def sorder(request):
    return render(request,'pos/order.html')  

def up_order_status(request, id):
    return render(request, 'sadmin/update_order_status.html')