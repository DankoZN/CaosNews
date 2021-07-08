from django.db import models

# Create your models here.

class Colaborador (models.Model):
    rutColaborador= models.IntegerField(primary_key=True, verbose_name='Rut colaborador')
    imagen= models.ImageField(upload_to='img/', null=True, blank=True)
    nomColaborador= models.CharField(max_length=60, verbose_name='Nombre colaborador')
    fonoColaborador= models.IntegerField( verbose_name='Telefono colaborador')
    dirColaborador= models.CharField(max_length=60, verbose_name= 'Dirección colaborador')
    emailColaborador= models.EmailField(verbose_name='E-mail colaborador')
    paisColaborador= models.CharField(max_length=60, verbose_name='País colaborador')
    contrasenaColaborador= models.CharField(max_length=20, verbose_name='Contraseña')

    def __str__(self):
        return self.nomColaborador