from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# Create your views here.
urlpatterns = [
    path('',views.add_dashboard, name='dashboard'), 
]