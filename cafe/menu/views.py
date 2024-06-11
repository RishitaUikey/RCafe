from django.shortcuts import render,redirect
from menu.models import menu
# Create your views here.

def menu(request):
    items = menu.objects.all()
    print(items)
    return render(request, 'menu.html', {'menu': items})

def addmenu(request):
    if request.method=='POST':
        food_category=request.POST.get('food_category')
        name=request.POST.get('name')  
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES['picture']
        if  food_category and name and quantity and price and image:
            store=menu.objects.create(food_category=food_category, name=name, price=price, quantity=quantity, picture=image)
        else :
            menu_items= menu.objects.all() # sequential data-type
            return render(request, 'menu.html',{'menu' : menu_items})
    
    p= menu.objects.all() # sequential data-type
    
    return render(request, 'menu/addmenu.html',{'menu' : p})


def delmenu(request,id):
  menu_items = menu.objects.filter(id = id)
  menu_items.delete()
  return redirect('menu/addmenu')

def upmenu(request,id):
    if request.method=='POST':
        food_category =request.POST.get('food_category')
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES.get('picture')
        id=request.POST.get('id')
        if id and  food_category and name and price and quantity and image:
            store=menu.objects.get(id=id)
            store.name=name
            store.food_category =food_category 
            store.price=price
            store.quantity=quantity
            if image:
                store.picture=image
            store.save()
            
            
            return redirect('menu/addmenu')
        else :
            pass
    
    menu_item= menu.objects.get(pk=id)
    return render(request,'menu/addmenu.html',{'menu_item':menu_item})

