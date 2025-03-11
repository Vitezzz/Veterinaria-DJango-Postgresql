from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaClientes, name='listaClientes'),
    path('create_persona/', views.create_persona, name='create_persona'),
    path('update_persona/<int:cve_persona>/', views.update_persona, name='update_persona'),
    path('delete_persona/<int:cve_persona>/', views.delete_persona, name='delete_persona'),
]