# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Citas(models.Model):
    cve_cita = models.IntegerField(primary_key=True)
    cve_veterinario = models.ForeignKey('Veterinarios', models.DO_NOTHING, db_column='cve_veterinario', blank=True, null=True)
    cve_mascota = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='cve_mascota', blank=True, null=True)
    sintomas = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    cancelada = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citas'


class Ciudades(models.Model):
    cve_ciudad = models.IntegerField(primary_key=True)
    cve_municipio = models.ForeignKey('Estados', models.DO_NOTHING, db_column='cve_municipio', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudades'


class Consultas(models.Model):
    cve_consulta = models.IntegerField(primary_key=True)
    cve_veterinario = models.ForeignKey('Veterinarios', models.DO_NOTHING, db_column='cve_veterinario', blank=True, null=True)
    cve_cliente = models.ForeignKey('Personas', models.DO_NOTHING, db_column='cve_cliente', blank=True, null=True)
    cve_mascota = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='cve_mascota', blank=True, null=True)
    cve_cita = models.ForeignKey(Citas, models.DO_NOTHING, db_column='cve_cita', blank=True, null=True)
    cve_motivo = models.ForeignKey('Motivos', models.DO_NOTHING, db_column='cve_motivo', blank=True, null=True)
    fecha_consulta = models.DateField(blank=True, null=True)
    diagnostico = models.CharField(max_length=300, blank=True, null=True)
    sintomas = models.CharField(max_length=200, blank=True, null=True)
    tratamiento = models.CharField(max_length=100, blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consultas'


class Especies(models.Model):
    cve_especie = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies'


class Estados(models.Model):
    cve_estado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Mascotas(models.Model):
    cve_mascota = models.IntegerField(primary_key=True)
    cve_raza = models.ForeignKey('Razas', models.DO_NOTHING, db_column='cve_raza', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    peso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    sexo = models.BooleanField(blank=True, null=True)
    imagen = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascotas'


class Modulos(models.Model):
    cve_modulo = models.IntegerField(primary_key=True)
    cve_tipo_modulo = models.ForeignKey('TiposModulos', models.DO_NOTHING, db_column='cve_tipo_modulo', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    liga = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulos'


class Motivos(models.Model):
    cve_motivo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motivos'


class Permisos(models.Model):
    cve_rol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='cve_rol', blank=True, null=True)
    cve_modulo = models.ForeignKey(Modulos, models.DO_NOTHING, db_column='cve_modulo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'


class Personas(models.Model):
    cve_persona = models.IntegerField(primary_key=True)
    cve_ciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='cve_municipio', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    paterno = models.CharField(max_length=50, blank=True, null=True)
    materno = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=70, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    imagen = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Razas(models.Model):
    cve_raza = models.IntegerField(primary_key=True)
    cve_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='cve_especie', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    foto = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'razas'


class Roles(models.Model):
    cve_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesUsuario(models.Model):
    cve_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='cve_rol', blank=True, null=True)
    cve_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='cve_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_usuario'


class Servicios(models.Model):
    cve_servicios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'servicios'


class ServiciosMascota(models.Model):
    cve_consulta = models.ForeignKey(Consultas, models.DO_NOTHING, db_column='cve_consulta', blank=True, null=True)
    cve_servicios = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='cve_servicios', blank=True, null=True)
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'servicios_mascota'


class TiposModulos(models.Model):
    cve_tipo_modulo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_modulos'


class Trabajadores(models.Model):
    cve_trabajador = models.OneToOneField(Personas, models.DO_NOTHING, db_column='cve_trabajador', primary_key=True)
    cve_turno = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='cve_turno', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajadores'


class TrabajadoresServicio(models.Model):
    cve_trabajador = models.ForeignKey(Trabajadores, models.DO_NOTHING, db_column='cve_trabajador', blank=True, null=True)
    cve_servicios = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='cve_servicios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajadores_servicio'


class Turnos(models.Model):
    cve_turno = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnos'


class Usuarios(models.Model):
    cve_usuarios = models.IntegerField(primary_key=True)
    cve_persona = models.ForeignKey(Personas, models.DO_NOTHING, db_column='cve_persona', blank=True, null=True)
    nombre_usuario = models.CharField(max_length=20, blank=True, null=True)
    contrsenha = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vacunas(models.Model):
    cve_vacunas = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacunas'


class VacunasMascotas(models.Model):
    cve_vacunas_mascotas = models.IntegerField(primary_key=True)
    cve_mascota = models.ForeignKey(Mascotas, models.DO_NOTHING, db_column='cve_mascota', blank=True, null=True)
    cve_vacunas = models.ForeignKey(Vacunas, models.DO_NOTHING, db_column='cve_vacunas', blank=True, null=True)
    fecha_aplicacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacunas_mascotas'


class Veterinarios(models.Model):
    cve_veterinarios = models.OneToOneField(Personas, models.DO_NOTHING, db_column='cve_veterinarios', primary_key=True)
    turno = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinarios'
