from django.urls import path
from . import views

urlpatterns = [
    path('addc/', views.add_cust, name='add_cust'),
    path('cdelete/<int:id>/', views.del_cust, name='del_cust'),
    path('cupdate/<int:id>/', views.up_cust, name='up_cust'),
]