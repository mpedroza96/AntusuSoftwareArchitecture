from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('catalogo/', views.catalogo_list),
    path('catalogocreate/', csrf_exempt(views.catalogo_create), name='catalogoCreate'),
]
