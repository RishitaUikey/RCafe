from django.urls import path
from menu.views import menu,addmenu,delmenu,upmenu
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', menu, name='menu'),
     path('addmenu/',addmenu,name='addmenu'),
    path('del/<int:id>/',delmenu,name='delmenu'),
    path('update/<int:id>/',upmenu,name='upmenu')
]