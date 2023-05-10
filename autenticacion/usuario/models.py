from django.db import models


class Usuario(models.Model):
    correo = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    


    def __str__(self):
        return '{}'.format(self.numHistoriaClinica)
# Create your models here.
