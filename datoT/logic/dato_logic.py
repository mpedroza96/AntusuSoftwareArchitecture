from ..models import Dato

def get_datos():
    queryset = Dato.objects.all().last()
    return (queryset)

def create_dato(form):
    measurement = form.save()
    measurement.save()
    return ()





