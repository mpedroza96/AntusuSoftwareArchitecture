from django.db import models

class Catalogo(models.Model):
    nombre = models.CharField(max_length=19)
    precio = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=110)

    def __str__(self):
        return '{}'.format(self.nombre)

