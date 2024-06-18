from datetime import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import POS

def add_cust(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        address = request.POST.get('Address')
        option_to_eat = request.POST.get('option_to_eat')

        if (customer_name and email and phone and address and option_to_eat):
            option_to_eat_valid= any(unit_choice[0] == option_to_eat for unit_choice in POS.UNIT_CHOICES)
            if not option_to_eat_valid:
                return render(request,'pos/add_cust.html')
            POS.objects.create(
                Customer_name=customer_name,
                Email=email,
                Phone=phone,
                Address=address,
                option_to_eat=option_to_eat,
                order_date=timezone.now() 
            )
            return redirect('pos/add_cust')
        else:
            add_customer = POS.objects.all()
            return render(request, 'pos/add_cust.html', {'add_cust': add_customer})

    add_customer = POS.objects.all()
    return render(request, 'pos/add_cust.html', {'add_cust': add_customer})

def del_cust(request, id):
    add_customer = POS.objects.get(id=id)
    add_customer.delete()
    return redirect('pos/add_cust.html', {'add_cust': add_customer})

def up_cust(request, id):
    add_customer = get_object_or_404(POS, id=id)
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        address = request.POST.get('Address')
        option_to_eat = request.POST.get('option_to_eat')
        
        if (customer_name and email and phone and address and option_to_eat):
            option_to_eat_valid = any(choice[0] == option_to_eat for choice in POS.OPTION_TO_EAT_CHOICES)
            if not option_to_eat_valid:
                return render(request, 'pos/edit_cust.html', {'error_message': 'Invalid option to eat selected.'})
                
            add_customer.Customer_name = customer_name 
            add_customer.Email = email
            add_customer.Phone = phone
            add_customer.Address = address
            add_customer.option_to_eat = option_to_eat
            add_customer.save()
            return redirect('up_cust', id=id)
    
    return render(request, 'pos/edit_cust.html', {'add_customer': add_customer})

