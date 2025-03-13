from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaClientes, name='listaClientes'),
    path('create_persona/', views.create_persona, name='create_persona'),
    path('update_persona/<int:cve_persona>/', views.update_persona, name='update_persona'),
    path('delete_persona/<int:cve_persona>/', views.delete_persona, name='delete_persona'),
    
    path('veterinarios/', views.listaVeterinarios, name='listaVeterinarios'),
    path('create_veterinario/', views.create_veterinario, name='create_veterinario'),  # Asegúrate de que el nombre sea correcto
    path('update_veterinario/<int:cve_veterinarios>/', views.update_veterinario, name='update_veterinario'),        
    path('delete_veterinario/<int:cve_veterinarios>/', views.delete_veterinario, name='delete_veterinario'),
    
    path('trabajadores/', views.listaTrabajadores, name='listaTrabajadores'),
    path('create_trabajador/', views.create_trabajador, name='create_trabajador'),  # Asegúrate de que el nombre sea correcto
    path('update_trabajador/<int:cve_trabajador>/', views.update_trabajador, name='update_trabajador'),  
    path('delete_trabajador/<int:cve_trabajador>/', views.delete_trabajador, name='delete_trabajador'),
      

]