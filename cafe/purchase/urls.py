from django.urls import path
from . import views

urlpatterns = [
    path('addp/', views.add_purchase, name='add_purchase'),
    path('pupdate/<int:id>/', views.upurchase, name='update_purchase'),
    path('pdelete/<int:id>/', views.dpurchase, name='delete_purchase'),
]
