from django.shortcuts import render, redirect
from purchase.models import Purchase

def add_purchase(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        item = request.POST.get('item')
        unit = request.POST.get('unit')
        quantity = request.POST.get('quantity')
        expiry_date = request.POST.get('expiry_date')
        price = request.POST.get('price')

        if (category and item and unit and quantity and expiry_date and price):
            store = Purchase.objects.create(category=category,item=item,unit=unit,quantity=quantity,expiry_date=expiry_date,price=price,
                total=float(quantity) * float(price)
            )
            
    purchase_item = Purchase.objects.all()
    return render(request, 'purchase/addp.html', {'purchase':purchase_item})

def dpurchase(request, id):
    store = Purchase.objects.get(id=id)
    store.delete()
    return redirect('purchase:addp')

def upurchase(request, id):
    if request.method == 'POST':
        category = request.POST.get('category')
        item = request.POST.get('item')
        unit = request.POST.get('unit')
        quantity = request.POST.get('quantity')
        expiry_date = request.POST.get('expiry_date')
        price = request.POST.get('price')
        if category and item and unit and quantity and expiry_date and price:
            store = Purchase.objects.get(id=id)
            store.category = category
            store.item = item
            store.unit = unit
            store.quantity = quantity
            store.expiry_date = expiry_date
            store.price = price
            store.total = float(quantity) * float(price)
            store.save()
            return redirect('purchase:edit_purchase')
        else:
            pass
    p = Purchase.objects.get(id=id)
    return render(request, 'purchase/edit_purchase.html', {'purchase': p})

