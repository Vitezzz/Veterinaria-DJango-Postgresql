from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mascotas'),
    path('create_mascota/', views.create_mascota, name='create_mascota'),
    path('update_mascota/<int:cve_mascota>/', views.update_mascota, name='update_mascota'),
    #path('update_especie/', views.update_especie, name='update_especie'),
    path('delete_mascota/<int:cve_mascota>/', views.delete_mascota, name='delete_mascota'),
    
]