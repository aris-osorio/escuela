from django.shortcuts import render
from django.http import HttpResponse
from clases.models import Clase
from estudiantes.models import Estudiante
from estudiantes.models import ListaClases

# Create your views here.
def clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases/clases.html', {'clases': clases})

def detalle_clase(request, clase_id):
    detalle = Clase.objects.get(id = clase_id)
    lista = ListaClases.objects.filter(clase = clase_id)
    return render(request, 'clases/detalle.html', {'clase': detalle, 'lista': lista})