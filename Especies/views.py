from django.shortcuts import render, redirect
from .models import Especies
from .models import Razas
from django.contrib import messages

# Create your views here.

def home(request):
    especies = Especies.objects.filter(activo=True).order_by('cve_especie')
    return render(request, 'gestionEspecies.html', {"especies": especies})

    
def create_especie(request):
    especie = Especies(nombre = request.POST['nombre'], descripcion = request.POST['descripcion'], imagen = request.FILES['imagen'])
    especie.save()
    messages.success(request, 'Especie cargada correctamente')
    return redirect('/especies/')

def edit_especie(request, cve_especie):
    especie = Especies.objects.get(cve_especie = cve_especie)
    return render(request, 'edicionEspecie.html', {"especie": especie})

def update_especie(request):
    cve_especie = request.POST['clave']
    especie = Especies.objects.get(cve_especie=cve_especie)
    especie.nombre = request.POST['nombre']
    especie.descripcion = request.POST['descripcion']
    imagen = request.FILES.get('imagen', None)
    if imagen:
        especie.imagen = imagen
    especie.save()
    messages.success(request, 'Especie actualizada correctamente')

    return redirect('/especies/')


def delete_especie(request, cve_especie):
    especie = Especies.objects.get(cve_especie=cve_especie)
    especie.activo = False
    especie.save()
    messages.success(request, 'Especie eliminada correctamente')

    return redirect('/especies/')

def gestionRazas(request):
    razas = Razas.objects.filter(activo=True).order_by('cve_especie')
    especies = Especies.objects.filter(activo=True).order_by('cve_especie')
    return render(request, 'gestionRazas.html', {'razas': razas, 'especies': especies})

def create_raza(request):
    cve_especie = request.POST['especie']
    especie = Especies.objects.get(cve_especie=cve_especie)
    raza = Razas(nombre=request.POST['nombre'], cve_especie=especie, foto=request.FILES['imagen'])
    raza.save()
    messages.success(request, 'Raza cargada correctamente')
    return redirect('/especies/gestionRazas/')

def edit_raza(request, cve_raza):
    raza = Razas.objects.get(cve_raza = cve_raza)
    especies = Especies.objects.filter(activo=True).order_by('cve_especie')
    return render(request, 'edicionRaza.html', {'raza': raza, 'especies': especies})

def update_raza(request):
    cve_raza = request.POST['clave']
    raza = Razas.objects.get(cve_raza=cve_raza)
    raza.nombre = request.POST['nombre']
    cve_especie = request.POST['especie']
    especie = Especies.objects.get(cve_especie=cve_especie)
    raza.cve_especie = especie
    foto = request.FILES.get('foto', None)
    if foto:
        raza.foto = foto
    raza.save()
    messages.success(request, 'Raza actualizada correctamente')
    return redirect('/especies/gestionRazas/')


def delete_raza(request, cve_raza):
    raza = Razas.objects.get(cve_raza=cve_raza)
    raza.activo = False
    raza.save()
    messages.success(request, 'Raza eliminada correctamente')

    return redirect('/especies/gestionRazas/')