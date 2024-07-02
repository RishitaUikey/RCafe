from django.shortcuts import render,redirect,get_object_or_404
from pos.models import POS, Order,OrderItem,Cart
from menu.models import amenu,category
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from cust.models import customer

@login_required
def add_cust(request):
        if request.method == 'POST':
            customer_name = request.POST.get('customer_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            option_to_eat = request.POST.get('option_to_eat')

            if customer_name and email and phone and address and option_to_eat:
                option_to_eat_valid = any(choice[0] == option_to_eat for choice in POS.OPTION_TO_EAT_CHOICES)
                if not option_to_eat_valid:
                    return render(request, 'pos/add_cust.html', {
                        'error_message': 'Invalid option to eat selected.',
                        'option_to_eat_choices': POS.OPTION_TO_EAT_CHOICES 
                    })
                        
                POS.objects.create(
                    Customer_name=customer_name,
                    Email=email,
                    Phone=phone,
                    Address=address,
                    option_to_eat=option_to_eat,
                    order_date=timezone.now()
                )
                return redirect('pos/add_cust')
            
        add_customer = POS.objects.all()
        return render(request, 'pos/add_cust.html', {
            'add_cust': add_customer,
            'option_to_eat_choices': POS.OPTION_TO_EAT_CHOICES 
            })

def del_cust(request, id):
    add_customer = get_object_or_404(POS, id=id)
    add_customer.delete()
    return redirect('pos/add_cust')

def up_cust(request, id):
    add_customer = get_object_or_404(POS, id=id)
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        address = request.POST.get('Address')
        option_to_eat = request.POST.get('option_to_eat')
        
        if customer_name and email and phone and address and option_to_eat:
            option_to_eat_valid = any(choice[0] == option_to_eat for choice in POS.OPTION_TO_EAT_CHOICES)
            if not option_to_eat_valid:
                return render(request, 'pos/edit_cust.html', {'error_message': 'Invalid option to eat selected.'})
                
            add_customer.customer_name = customer_name
            add_customer.email = email
            add_customer.phone = phone
            add_customer.address = address
            add_customer.option_to_eat = option_to_eat
            add_customer.save()
            return redirect('up_cust', id=id)
    
    return render(request, 'pos/edit_cust.html', {'add_customer': add_customer})


@login_required
def add_item_to_cart(request,p_id):
    pro=amenu.objects.get(pk=p_id)
    user=request.user
    cart_item,created=Cart.objects.get_or_create(user=user,productorder=pro,defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def buy_now(request, p_id):
    pro = get_object_or_404( amenu ,pk=p_id)
    user=request.user
    cart_item,created=Cart.objects.get_or_create(user=user,productorder=pro,defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def show_orders(request):
    last_order = Order.objects.filter(user=request.user).last()
    if last_order:
        order_items = last_order.orderitem_set.all()
        total_price = sum(item.quantity * item.menuorder.price for item in order_items)
    else:
        order_items = []
        total_price = 0
    return render(request, 'pos/cart.html', {'order_items': order_items, 'total_price': total_price})


@login_required
def manage_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total for item in cart_items)

    if request.method == 'POST':
        for item in cart_items:
            order_date = timezone.now().date()
            order, created = Order.objects.get_or_create(user=request.user, created_at__date=order_date, defaults={'total_amount': total_price})
            if not created:
                order.total_amount += float(item.total)
                order.save()
            order_item, item_created = OrderItem.objects.get_or_create(order=order, menuorder=item.productorder, defaults={'quantity': item.quantity})
            if not item_created:
                order_item.quantity += item.quantity
                order_item.save()
            item.delete()
        return redirect('cart')

    return render(request, 'pos/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def confirm_order(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        print(cart_items)
    
    return render(request, 'customer/confirm_order.html')


@login_required
def increase_cart_quantity(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required
def decrease_cart_quantity(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')


@login_required
def delete_cart_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart')

# def myorders(request):
#     user = request.user
#     orders = OrderItem.objects.filter(order__in=orders.objects.filter(user=user)).order_by("-id")  

#     context = {
#         'user': user,
#         'orders': orders,
#     }
#     return render(request, 'customer/myorder.html',context)

@login_required
def myorders(request):
    user = request.user
    user_orders = Order.objects.filter(user=user)  # Use a different variable name to avoid conflict
    orders = OrderItem.objects.filter(order__in=user_orders).order_by("-id")
    return render(request, 'pos/myorder.html', {'orders': orders})

@login_required
def profile(request):
    user = request.user
    orders = OrderItem.objects.filter(order__in=orders.objects.filter(user=user))  

    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'customer/profilepage.html',context)



# @login_required
# def cprofile(request):
#     user_profile, created = customer.objects.get_or_create(user=request.user)

#     if request.method == 'POST':
#         form = custname(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('userprofile')
#     else:
#         form = custname(instance=user_profile)

#    # orders = order.objects.filter(user=request.user)  # Assuming you have an Order model

#     context = {
#         'form': form,
#         'user': request.user,
#         'profile': user_profile,
#         #'orders': orders
#     }

#     return render(request, 'customer/custform.html', context)

@login_required
def up_order_status(request, id):
    if request.method == 'POST':
        sstatus = request.POST.get('status')
        store = get_object_or_404(Order, id=id)
        store.status = sstatus
        store.save()
        return redirect('/pos/order')
    else:
        s = get_object_or_404(Order, pk=id)
        return render(request, 'pos/order_status.html', {'ser': s})

def sorder(request):
    item = Order.objects.all().order_by('-created_at') 
    return render(request,'pos/order.html', {'item': item})  

def conform_order(request):
    if request.method == 'POST':
        mycart=Cart.objects.filter(user=request.user)
        print(mycart)