from django.db import models
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

    class Meta:
        managed = False
        db_table = 'razas'
