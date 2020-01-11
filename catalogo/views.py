from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CatalogoForm
from .logic.catalogo_logic import get_catalogos, create_catalogo


def catalogo_list(request):
    measurements = get_catalogos()
    context = {
        'catalogo_list': measurements
    }
    return render(request, 'Catalogo/catalogo.html', context)

def catalogo_create(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST)
        if form.is_valid():
            create_catalogo(form)
            messages.add_message(request, messages.SUCCESS, 'Producto create successful')
            return HttpResponseRedirect(reverse('catalogoCreate'))
        else:
            print(form.errors)
    else:
        form = CatalogoForm()

    context = {
        'form': form,
    }

    return render(request, 'Catalogo/catalogoCreate.html', context)