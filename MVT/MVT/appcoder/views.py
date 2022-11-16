from datetime import datetime

from appcoder.forms import *
from appcoder.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def inicio(request):
    return render(request, 'appcoder/inicio.html')


def familiares(request):
    familia = familiar.objects.all()
    
    # respuesta = ""
    # for i in familiares:
    #     respuesta += i.nombre  #+ i.edad + " " + i.fecha + " | "
    
    # creo lista para iterar mejor con el loop en el template
    respuesta = []
    for i in familia:
        respuesta.append(i.nombre + ", " + str(i.edad) + " anios, " + "su primer competicion olimpica fue " + str(i.fecha))

    return render(request, 'appcoder/familiares.html', {'familiares':familia, 'respuesta':respuesta})  # render(request, 'appcoder/familia.html')


def deportes(request):
    deportes = deporte.objects.all()

    respuesta = []
    for d in deportes:
        respuesta.append(d.nombre + ", se juega de a " + str(d.cantidad_jugadores) + " jugadores.")
    
    return render(request, 'appcoder/deportes.html', {'deporte':respuesta, 'deportes':deportes})


def equipos(request):
    equipos = equipo.objects.all()

    respuesta = []
    for e in equipos:
        respuesta.append(e.nombre + ", ha ganado " + str(e.cantidad_medallas) + " de medallas olimpicas.")
    
    return render(request, 'appcoder/equipos.html', {'equipo': respuesta})


# FORMULARIOS

def familiaFormulario(request):
    if request.method == 'POST':
        formulario = FamiliaFormulario(request.POST) #aqui llega la info del html
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            familia = familiar(nombre=informacion['nombre'], edad=informacion['edad'], fecha=informacion['fecha'])
            familia.save()
            return render(request, 'appcoder/familiares.html')
    else:
        formulario=FamiliaFormulario()
    return render(request, 'appcoder/formsfamilia.html', {'formulario':formulario})


def deportesFormulario(request):
    formulario = DeportesFormulario(request.POST)
    if request.method == "POST" and formulario.is_valid():
        #info = formulario.cleaned_data
        nombre=formulario.cleaned_data['nombre']
        jugadores=formulario.cleaned_data['jugadores']
        deportes = deporte(nombre=nombre, cantidad_jugadores=jugadores)
        deportes.save()
        return render(request, 'appcoder/deportes.html')
    else:
        formulario=DeportesFormulario()
    return render(request, 'appcoder/formsdeportes.html', {'formulario':formulario})
    

def equiposFormulario(request):
    formulario = EquiposFormulario(request.POST)
    if request.method == "POST" and formulario.is_valid():
        info = formulario.cleaned_data
        equipos = equipo(nombre=info['nombre'], cantidad_medallas=info['medallas'])
        equipos.save()
        return render(request, 'appcoder/equipos.html')
    else:
        formulario=EquiposFormulario()
    return render(request, 'appcoder/formsequipos.html', {'formulario':formulario})