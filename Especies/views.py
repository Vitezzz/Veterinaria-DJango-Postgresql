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
    return redirect('/')

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

    return redirect('/')


def delete_especie(request, cve_especie):
    especie = Especies.objects.get(cve_especie=cve_especie)
    especie.activo = False
    especie.save()
    messages.success(request, 'Especie eliminada correctamente')

    return redirect('/')