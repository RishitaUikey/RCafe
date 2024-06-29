from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('addc/', views.add_cust, name='add_cust'),
    # path('cdelete/<int:id>/', views.del_cust, name='del_cust'),
    # path('cupdate/<int:id>/', views.up_cust, name='up_cust'),
    path('buy_now/<int:p_id>/', views.buy_now, name='buy_now'),
    path('add/<int:p_id>/', views.add_item_to_cart, name='add_item_to_cart'),
    path('cart/', views.manage_cart, name='cart'),
    path('corder/', views.confirm_order, name='corder'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('increase_quantity/<int:cart_id>/', views.increase_cart_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_id>/', views.decrease_cart_quantity, name='decrease_quantity'),
    path('delete_item/<int:cart_id>/', views.delete_cart_item, name='delete_item'),
    
    path('myorder',views.myorders, name='myorder'),
    path('oconform/', views.conform_order, name='order'),
    path('status/<int:id>/', views.up_order_status, name='order_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
