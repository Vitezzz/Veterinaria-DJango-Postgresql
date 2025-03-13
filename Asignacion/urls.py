from django.urls import path
from . import views

urlpatterns = [
    path('listaMotivos/', views.listaMotivos, name='listaMotivos'),
    path('create_motivo/', views.create_motivo, name='create_motivo'),
    path('update_motivo/<int:cve_motivo>/', views.update_motivo, name='update_motivo'),
    path('delete_motivo/<int:cve_motivo>/', views.delete_motivo, name='delete_motivo'),
      
]