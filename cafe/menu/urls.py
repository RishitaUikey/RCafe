from django.urls import path
from menu.views import menuu,addmenu,delmenu,upmenu
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', menuu, name='menu'),
     path('addmenu/',addmenu,name='addmenu'),
    path('del/<int:id>/',delmenu,name='delmenu'),
    path('update/<int:id>/',upmenu,name='upmenu'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)