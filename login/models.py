from django.db import models
# Create your models here.



class Usuario(models.Model):
    cod_usuario = models.CharField(primary_key=True, max_length=50, db_column="cod_usuario")
    nombre = models.CharField(max_length=50, blank=True, null=True, db_column="nombre")
    apellido = models.CharField(max_length=50, blank=True, null=True, db_column="apellido")
    password = models.CharField(max_length=50, blank=True, null=True, db_column="password")

    class Meta:
        managed = False
        db_table = 'usuario'
