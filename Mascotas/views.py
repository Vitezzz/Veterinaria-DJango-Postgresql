from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascotas, Razas
from django.contrib import messages
from datetime import datetime

# Create your views here.

def home(request):
    mascotas = Mascotas.objects.filter(activo=True).order_by('cve_mascota')
    razas = Razas.objects.filter(activo=True).order_by('cve_raza')
    return render(request, 'Mascotas/gestionMascotas.html', {"mascotas": mascotas})

def create_pet (request):
    razas = Razas.objects.filter(activo=True).order_by('cve_raza')
    return render (request, 'Mascotas/crearMascota.html', {"razas": razas})

def create_mascota(request):
    if request.method == "POST":
        cve_raza = request.POST['raza']
        raza = Razas.objects.get(cve_raza=cve_raza)
        fecha_nac = datetime.strptime(request.POST['fecha'], '%Y-%m-%dT%H:%M')
        mascota = Mascotas(
            cve_raza=raza,
            nombre=request.POST['nombre'],
            peso=request.POST['peso'],
            fecha_nac=fecha_nac,
            sexo=request.POST['sexo'],
            imagen=request.FILES['imagen']
        )
        mascota.save()
        messages.success(request, 'Mascota cargada correctamente')
        return redirect('/mascotas/')
    else:
        razas = Razas.objects.filter(activo=True).order_by('cve_raza')
        return render(request, 'Mascotas/crearMascota.html', {"razas": razas})

def update_mascota(request, cve_mascota):
    mascota = get_object_or_404(Mascotas, cve_mascota=cve_mascota)
    if request.method == "POST":
        cve_raza = request.POST['raza']
        raza = Razas.objects.get(cve_raza=cve_raza)
        fecha_nac = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
        mascota.cve_raza = raza
        mascota.nombre = request.POST['nombre']
        mascota.peso = request.POST['peso']
        mascota.fecha_nac = fecha_nac
        mascota.sexo = request.POST['sexo']
        if 'imagen' in request.FILES:
            mascota.imagen = request.FILES['imagen']
        mascota.save()
        messages.success(request, 'Mascota actualizada correctamente')
        return redirect('mascotas')
    else:
        razas = Razas.objects.filter(activo=True).order_by('cve_raza')
        return render(request, 'Mascotas/editarMascota.html', {"mascota": mascota, "razas": razas})
    
def delete_mascota(request, cve_mascota):
    mascotas = Mascotas.objects.get(cve_mascota=cve_mascota)
    mascotas.activo = False
    mascotas.save()
    messages.success(request, 'Mascota eliminada correctamente')

    return redirect('mascotas')
