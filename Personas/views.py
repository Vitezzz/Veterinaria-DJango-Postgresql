from django.shortcuts import render, get_object_or_404, redirect
from .models import Personas, Municipios, Turnos, Veterinarios, Trabajadores
from django.contrib import messages
from datetime import datetime


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

def listaVeterinarios(request):
    veterinarios = Veterinarios.objects.filter(activo=True).select_related('cve_veterinarios', 'cve_turno').order_by('cve_veterinarios')
    return render(request, 'Veterinario/listadoVeterinarios.html', {"veterinarios": veterinarios})

def create_veterinario(request):
    if request.method == "POST":
        cve_turno = request.POST['turno']
        turnos = Turnos.objects.get(cve_turno=cve_turno)
        cve_persona = request.POST['persona']
        personas = Personas.objects.get(cve_persona=cve_persona)
        
        # Verificar si la persona ya está registrada como veterinario
        if Veterinarios.objects.filter(cve_veterinarios=personas).exists():
            messages.error(request, 'La persona ya está registrada como veterinario')
            return redirect('create_veterinario')
        
        fecha_ingreso = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
        veterinarios = Veterinarios(
            cve_veterinarios=personas,
            fecha_ingreso=fecha_ingreso,
            cve_turno=turnos
        )
        veterinarios.save()
        messages.success(request, 'Veterinario cargado correctamente')
        return redirect('/personas/veterinarios/')
    else:
        turnos = Turnos.objects.all().order_by('cve_turno')
        personas = Personas.objects.filter(activo=True).order_by('cve_persona')
        return render(request, 'Veterinario/crearVeterinario.html', {"turnos": turnos, "personas": personas})
    
def update_veterinario(request, cve_veterinarios):
    veterinarios = get_object_or_404(Veterinarios, cve_veterinarios=cve_veterinarios)
    if request.method == "POST":
        cve_turno = request.POST['turno']
        turnos = Turnos.objects.get(cve_turno=cve_turno)
        fecha_ingreso = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
        veterinarios.cve_turno = turnos
        veterinarios.fecha_ingreso = fecha_ingreso
        veterinarios.save()
        messages.success(request, 'Veterinario actualizado correctamente')
        return redirect('/personas/veterinarios/')
    else:
        turnos = Turnos.objects.all().order_by('cve_turno')
        personas = Personas.objects.filter(activo=True).order_by('cve_persona')
        return render(request, 'Veterinario/editarVeterinario.html', {"veterinarios": veterinarios, "turnos": turnos, "personas": personas})
    
def delete_veterinario(request, cve_veterinarios):
    veterinarios = Veterinarios.objects.get(cve_veterinarios=cve_veterinarios)
    veterinarios.activo = False
    veterinarios.save()
    messages.success(request, 'Veterinario eliminado correctamente')

    return redirect('/personas/veterinarios')    