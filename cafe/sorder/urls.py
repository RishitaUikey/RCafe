from django.urls import path
from sorder.views import sorder
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', sorder, name='sorder'),
]
