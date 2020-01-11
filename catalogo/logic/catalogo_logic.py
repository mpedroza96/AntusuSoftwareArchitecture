from ..models import Catalogo

def get_catalogos():
    queryset = Catalogo.objects.all()
    return (queryset)

def create_catalogo(form):
    measurement = form.save()
    measurement.save()
    return ()





