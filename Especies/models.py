from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


# Create your models here.

class Especies(models.Model):
    cve_especie = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.ImageField(upload_to='especies/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'especies'
        


class Razas(models.Model):
    cve_raza = models.AutoField(primary_key=True)
    cve_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='cve_especie', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='razas/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'razas'
        
        
@receiver(pre_save, sender=Razas)
def set_custom_cve_raza(sender, instance, **kwargs):
    if not instance.cve_raza:
        # Obtener el valor máximo actual de cve_raza
        max_cve_raza = Razas.objects.aggregate(models.Max('cve_raza'))['cve_raza__max']
        if max_cve_raza is None:
            # Si no hay registros, empezar desde el valor deseado
            instance.cve_raza = 2  # Cambia este valor al que desees
        else:
            # Incrementar el valor máximo en 1
            instance.cve_raza = max_cve_raza + 1
            
@receiver(pre_save, sender=Especies)
def set_custom_cve_especie(sender, instance, **kwargs):
    if not instance.cve_especie:
        # Obtener el valor máximo actual de cve_especie
        max_cve_especie = Especies.objects.aggregate(models.Max('cve_especie'))['cve_especie__max']
        if max_cve_especie is None:
            # Si no hay registros, empezar desde el valor deseado
            instance.cve_especie = 7  # Cambia este valor al que desees
        else:
            # Incrementar el valor máximo en 1
            instance.cve_especie = max_cve_especie + 1
