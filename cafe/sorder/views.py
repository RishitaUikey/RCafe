
from django.shortcuts import render,redirect

# Create your views here.

def sorder(request):
    i = sorder.objects.all()
    return render(request, 'order.html', {'sorder': i})