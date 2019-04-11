from django.shortcuts import render
from .models import *

def inicio(request):
    context = {}
    context["inicio"] = Compra.objects.all()

    return render(request, "inicio.html", context)

def todosdeta(request, compras):
    
	
	context = {}
	context["todosdeta"] = Compra.objects.all()

	return render(request, "detalle.html", context)
# Create your views here.
