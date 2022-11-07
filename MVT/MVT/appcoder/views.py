from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appcoder.models import familiar

from datetime import datetime

# def familia(request):
#     lista_nombres= ['familiar1', 'familiar2', 'familiar3']
#     lista_edad= [25,32,45]
#     lista_recibimiento=["2020-12-01","2015-12-02","2000-12-02"]
#     familia = {"nombre":lista_nombres, "edad": lista_edad, "fecha_recibimiento":lista_recibimiento}
    
#     plantilla = loader.get_template("inicio.html")
#     documento = plantilla.render(familia)

#     return HttpResponse(documento)


def inicio(request):
    return render(request, 'appcoder/inicio.html')


def familia(request):
    familiares = familiar.objects.all()
    
    # for i in familiares:
    #     respuesta += i.nombre  #+ i.edad + " " + i.fecha + " | "
    
    # AL FALLAR LOGICA ANTERIOR EN respuesta PRUEBO OTRAS LOGICAS
    respuesta = []
    for i in familiares:
        respuesta.append(i.nombre + ", " + str(i.edad) + " anios, " + "su fecha de graduacion fue " + str(i.fecha))

    return render(request, 'appcoder/coder.html', {'familiares':familiares, 'respuesta':respuesta})  # render(request, 'appcoder/familia.html')