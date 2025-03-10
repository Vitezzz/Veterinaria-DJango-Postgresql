from django.db import models

class Mascotas(models.Model):
    cve_mascota = models.AutoField(primary_key=True)
    cve_raza = models.ForeignKey('Razas', models.DO_NOTHING, db_column='cve_raza', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    peso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    sexo = models.BooleanField(blank=True, null=True)
    imagen = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'mascotas'
        
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
        

# Create your models here.
