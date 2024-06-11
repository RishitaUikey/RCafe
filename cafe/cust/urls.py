from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/',views.login_user, name='login'), # url for login
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    
]