from django.shortcuts import render, get_object_or_404, redirect
from .models import Personas, Municipios
from django.contrib import messages

# Create your views here.

def listaClientes(request):
    personas = Personas.objects.filter(activo=True).order_by('cve_persona')
    return render(request, 'Clientes/listadoClientes.html', {"personas": personas})

def create_persona(request):
    if request.method == "POST":
        cve_municipio = request.POST['municipio']
        municipios = Municipios.objects.get(cve_municipio=cve_municipio)
        personas = Personas(
            nombre=request.POST['nombre'],
            paterno=request.POST['paterno'],
            materno=request.POST['materno'],
            direccion=request.POST['direccion'],
            correo=request.POST['correo'],
            telefono=request.POST['direccion'],
            imagen=request.FILES['imagen'],
            cve_municipio=municipios

        )
        personas.save()
        messages.success(request, 'Persona cargada correctamente')
        return redirect('/personas/')
    else:
        municipios = Municipios.objects.filter(activo=True).order_by('cve_municipio')
        return render(request, 'Clientes/crearPersona.html', {"municipios": municipios})
    
def update_persona(request, cve_persona):
    personas = get_object_or_404(Personas, cve_persona=cve_persona)
    if request.method == "POST":
        cve_municipio = request.POST['municipio']
        municipios = Municipios.objects.get(cve_municipio=cve_municipio)
        personas.cve_municipio = municipios
        personas.nombre = request.POST['nombre']
        personas.paterno = request.POST['paterno']
        personas.materno = request.POST['materno']
        personas.direccion = request.POST['direccion']
        personas.correo= request.POST['correo']
        personas.telefono = request.POST['telefono']
        if 'imagen' in request.FILES:
            personas.imagen = request.FILES['imagen']
        personas.save()
        messages.success(request, 'Persona actualizada correctamente')
        return redirect('/personas/')
    else:
        municipios = Municipios.objects.filter(activo=True).order_by('cve_municipio')
        return render(request, 'Clientes/editarPersona.html', {"personas": personas, "municipios": municipios})
    
def delete_persona(request, cve_persona):
    personas = Personas.objects.get(cve_persona=cve_persona)
    personas.activo = False
    personas.save()
    messages.success(request, 'Persona eliminada correctamente')

    return redirect('/personas/')