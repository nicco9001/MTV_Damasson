from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from Mi_APP.models import Familia

def prueba(request):
    return HttpResponse(f"Hola Mundo")

def listar_familia(request):
    context = {}
    context["familiares"] = Familia.objects.all()
    return render(request, "Mi_APP/familia.html", context)

# Create your views here.
