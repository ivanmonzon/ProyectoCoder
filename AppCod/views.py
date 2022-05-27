from django.http import HttpResponse
from AppCod.models import Curso
# Create your views here.
def curso(self):
    curso=Curso(nombre="Desarrollo Web", camada=2)
    curso.save()
    documentoDeTexto = f"--->Curso:  {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)