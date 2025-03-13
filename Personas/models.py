from django.db import models

# Create your models here.
class Estados(models.Model):
    cve_estado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'estados'
        
class Municipios(models.Model):
    cve_municipio = models.IntegerField(primary_key=True)
    cve_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='cve_estado', blank=True, null=True)  # Cambiar db_column a 'cve_estado'
    nombre = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'municipios'
        
class Personas(models.Model):
    cve_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    paterno = models.CharField(max_length=50, blank=True, null=True)
    materno = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=70, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    imagen = models.ImageField(upload_to='dueños/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    cve_municipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='cve_municipio', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'personas'



class Turnos(models.Model):
    cve_turno = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnos'
        
class Veterinarios(models.Model):
    cve_veterinarios = models.OneToOneField(Personas, on_delete=models.DO_NOTHING, primary_key=True, db_column='cve_veterinarios')
    fecha_ingreso = models.DateField(blank=True, null=True)
    cve_turno = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='cve_turno', blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'veterinarios'
        
class Trabajadores(models.Model):
    cve_trabajador = models.OneToOneField(Personas, models.DO_NOTHING, db_column='cve_trabajador', primary_key=True)
    cve_turno = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='cve_turno', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'trabajadores'
        