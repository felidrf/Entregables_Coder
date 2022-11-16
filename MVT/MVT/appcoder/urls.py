from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("familiares/", familiares, name="familiares"),
    path("deportes/", deportes, name="deportes"),
    path("equipos/", equipos, name="equipos"),
    
    path("formsfamilia/", familiaFormulario, name='formsfamilia'),
    path("formsdeportes/", deportesFormulario, name='formsdeportes'),
    path("formsequipos/", equiposFormulario, name='formsequipos'),
]
