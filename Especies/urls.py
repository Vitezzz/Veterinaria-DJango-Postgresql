from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_especie/', views.create_especie, name='create_especie'),
    path('edit_especie/<int:cve_especie>/', views.edit_especie, name='edit_especie'),
    path('update_especie/', views.update_especie, name='update_especie'),
    path('delete_especie/<int:cve_especie>/', views.delete_especie, name='delete_especie'),
]