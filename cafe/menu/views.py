from django.shortcuts import render,redirect
from menu.models import amenu,category
# Create your views here.

def menuu(request):
    items = amenu.objects.all()
    print(items)
    return render(request, 'customer/menu.html', {'menu': items})

def addmenu(request):
    if request.method=='POST':
        food_category_id=request.POST.get('food_category')
        name=request.POST.get('name')  
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES['picture']
        if  food_category_id and name and quantity and price and image :
            food_category = category.objects.get(id=food_category_id)
            store = amenu.objects.create(food_category=food_category, name=name, price=price, quantity=quantity, picture=image)
            store.save()
            return render(request, 'menu/addmenu.html')
        else :
            menu_items= amenu.objects.all() # sequential data-type
            return render(request, 'menu/addmenu.html',{'menu' : menu_items})
    
    p= amenu.objects.all() # sequential data-type
    categories = category.objects.all()
    return render(request, 'menu/addmenu.html',{'menu' : p, 'categories': categories})


def delmenu(request,id):
  menu_items = amenu.objects.filter(id = id)
  menu_items.delete()
  return redirect('menu/addmenu')

def upmenu(request,id):
    if request.method=='POST':
        food_category_id =request.POST.get('food_category')
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES.get('picture')
        menu_item = amenu.objects.get(id=id)

        if food_category_id and name and price and quantity:
            food_category = category.objects.get(id=food_category_id)
            store=amenu.objects.get(id=id)
            store.name=name
            store.food_category =food_category 
            store.price=price
            store.quantity=quantity
            if image:
                store.picture=image
            store.save()
            return redirect('menu/edit_menu')
        else :
            pass
    
    menu_item= amenu.objects.get(pk=id)
    categories = category.objects.all()
    return render(request,'menu/edit_menu.html',{'menu_item':menu_item, 'categories': categories})

