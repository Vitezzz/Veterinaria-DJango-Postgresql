from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='especies'),
    path('create_especie/', views.create_especie, name='create_especie'),
    path('edit_especie/<int:cve_especie>/', views.edit_especie, name='edit_especie'),
    path('update_especie/', views.update_especie, name='update_especie'),
    path('delete_especie/<int:cve_especie>/', views.delete_especie, name='delete_especie'),
    
    path('gestionRazas/', views.gestionRazas, name='razas'),
    path('gestionRazas/create_raza/', views.create_raza, name='create_raza'),
    path('gestionRazas/edit_raza/<int:cve_raza>/', views.edit_raza, name='edit_raza'),
    path('gestionRazas/update_raza/', views.update_raza, name='update_raza'),
    path('gestionRazas/delete_raza/<int:cve_raza>/', views.delete_raza, name='delete_raza'),

]