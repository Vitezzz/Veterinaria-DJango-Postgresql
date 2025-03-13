from django.db import models


# Create your models here.
class Motivos(models.Model):
    cve_motivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)


    class Meta:
        managed = False
        db_table = 'motivos'