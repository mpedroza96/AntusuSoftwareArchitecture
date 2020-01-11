from django import forms
from .models import Dato

class DatoForm(forms.ModelForm):
    class Meta:
        model = Dato
        fields = [
            'numeroTarjeta',
            'fechaCaducidadM',
            'fechaCaducidadA',
            'codigoSeguridad',
        ]
        labels = {
            'numeroTarjeta': 'Numero Tarjeta',
            'fechaCaducidadM': 'Mes Caducidad',
            'fechaCaducidadA': 'Año Caducidad',
            'codigoSeguridad': 'CVV',
        }