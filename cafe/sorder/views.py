from django.shortcuts import render,redirect,  get_object_or_404
from menu.models import amenu
from django.contrib.auth.decorators import login_required
from .models import order, orderitem, cart
from django.contrib.auth.models import User
from sorder.models import order
# Create your views here.

# Add to Cart View
@login_required
def add_to_cart(request, menu_id):
    menu_item = get_object_or_404(amenu, id=menu_id)
    cart_item, created = cart.objects.get_or_create(user=request.user, menu_orderedorder=menu_item)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('sorder/cart')

# Cart View
@login_required
def cart(request):
    cart_items = cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.menu_orderedorder.price for item in cart_items)
    return render(request, 'sorder/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Checkout View
@login_required
def checkout(request):
    cart_items = cart.objects.filter(user=request.user)
    if request.method == 'POST':
        new_order = order.objects.create(
            user=request.user,
            order_id=order.objects.count() + 1,
            total=sum(item.quantity * item.menu_orderedorder.price for item in cart_items)
        )
        for item in cart_items:
            orderitem.objects.create(
                order=new_order,
                menu_ordered=item.menu_orderedorder,
                quantity=item.quantity,
                total_price=item.quantity * item.menu_orderedorder.price
            )
        cart_items.delete()
        return redirect('order_confirmation', order_id=new_order.id)
    return render(request, 'sorder/checkout.html', {'cart_items': cart_items})

# Order Confirmation View
@login_required
def order_confirmation(request, order_id):
    order_details = get_object_or_404(order, id=order_id)
    return render(request, 'sorder/confirmation.html', {'order': order_details})

# Order List View
@login_required
def order_list(request):
    orders = order.objects.filter(user=request.user)
    return render(request, 'sorder/order_list.html', {'orders': orders})

# Order Detail View
@login_required
def order_detail(request, order_id):
    order_details = get_object_or_404(order, id=order_id)
    order_items = orderitem.objects.filter(order=order_details)
    return render(request, 'sorder/order_detail.html', {'order': order_details, 'order_items': order_items})
