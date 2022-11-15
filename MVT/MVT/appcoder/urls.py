from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("familiares/", familiares, name="familiares"),
    path("deportes/", deportes, name="deportes"),
    path("equipos/", equipos, name="equipos"),
    
    #path("cursos/", cursos),
    #path("entregables/", entregables),
]
