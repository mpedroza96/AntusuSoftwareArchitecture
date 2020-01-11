from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import DatoForm
from .logic.dato_logic import get_datos, create_dato
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

def dato_list(request):
    measurements = get_datos()
    context = {
        'dato_list': measurements
    }
    return render(request, 'Catalogo/datoT.html', context)

def dato_create(request):
    if request.method == 'POST':
        form = DatoForm(request.POST)
        info = form.__getitem__('numeroTarjeta').value()+form.__getitem__('fechaCaducidadM').value()+form.__getitem__('fechaCaducidadA').value()+form.__getitem__('codigoSeguridad').value()
        print(info.__hash__())
        if form.is_valid():
            create_dato(form)
            measurements = get_datos()
            info2 = measurements.numeroTarjeta + measurements.fechaCaducidadM + measurements.fechaCaducidadA + measurements.codigoSeguridad
            print(info2.__hash__())

            messages.add_message(request, messages.SUCCESS, 'Data create successful')
            return HttpResponseRedirect(reverse('datoCreate'))
        else:
            print(form.errors)
    else:
        form = DatoForm()

    context = {
        'form': form,
    }

    return render(request, 'Catalogo/catalogoCreate.html', context)