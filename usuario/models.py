from django.db import models

class Usuario(models.Model):
    correo = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.correo)


