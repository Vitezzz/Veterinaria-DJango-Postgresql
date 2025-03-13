from django.shortcuts import render, get_object_or_404, redirect
from .models import Motivos
from django.contrib import messages
from datetime import datetime


# Create your views here.

def listaMotivos(request):
    motivos = Motivos.objects.filter(activo=True).order_by('cve_motivo')
    return render(request, 'Motivos/listaMotivos.html', {"motivos": motivos})

def create_motivo(request):
    if request.method == "POST":
        motivos = Motivos(
            nombre=request.POST['nombre'],
        )
        motivos.save()
        messages.success(request, 'Motivo cargado correctamente')
        return redirect('/asignacion/listaMotivos/')
    else:
        return render(request, 'Motivos/crearMotivo.html')

def update_motivo(request, cve_motivo):
    motivo = get_object_or_404(Motivos, cve_motivo=cve_motivo)
    if request.method == "POST":
        motivo.nombre = request.POST['nombre']
        motivo.save()
        messages.success(request, 'Motivo actualizado correctamente')
        return redirect('listaMotivos')
    else:
        return render(request, 'Motivos/editarMotivo.html', {"motivo": motivo})
    
def delete_motivo(request, cve_motivo):
    motivos = Motivos.objects.get(cve_motivo=cve_motivo)
    motivos.activo = False
    motivos.save()
    messages.success(request, 'Motivo eliminado correctamente')

    return redirect('/asignacion/listaMotivos/')