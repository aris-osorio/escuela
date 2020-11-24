from django.shortcuts import render
from django.http import HttpResponse
from estudiantes.models import Estudiante
from estudiantes.models import ListaClases

# Create your views here.
def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    detalle = Estudiante.objects.get(id = estudiante_id)
    lista = ListaClases.objects.filter(estudiante = estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': detalle, 'lista': lista})