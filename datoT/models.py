from django.db import models

class Dato(models.Model):
    numeroTarjeta = models.CharField(max_length=19)
    fechaCaducidadM = models.CharField(max_length=2)
    fechaCaducidadA = models.CharField(max_length=2)
    codigoSeguridad = models.CharField(max_length=3)

    def __str__(self):
        return '{}'.format(self.numeroTarjeta)

