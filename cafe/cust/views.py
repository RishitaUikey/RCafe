from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from cust.forms import SignUpForm, SignUpForm
# Create your views here.
def home(request):
    return render(request, 'customer/home.html')

def login_user(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Login Successful !!!'))
            return redirect('home')
        else:
            messages.success(request,('Login UN-Successful !!!'))
            return redirect('login')
    else:
        return render(request, 'customer/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,(" You have successfully loged out"))
    return render(request, 'customer/login.html')

# register page 
def register_user(request):
    form=SignUpForm()
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Successful, and Logined in..'))
            return redirect('cust_home')
        else:
            messages.success(request,('Registration Un-Successful, try again..'))
            return redirect('register')
    return render(request, 'customer/register.html',{'form': form})

