from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('datocreate/', csrf_exempt(views.dato_create), name='datoCreate'),
]
