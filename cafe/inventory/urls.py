from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('add/', views.add_inventory, name='add_inventory'),
    path('idelete/<int:id>/', views.dinventory, name='delete_inventory'),
    path('iupdate/<int:id>/', views.uinventory, name='update_inventory'),
]
