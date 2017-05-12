from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.

def home(request):
	base_datos = Pages.objects.all()
	respuesta = "<h1>" + "Contenidos" + "</h1>"
	respuesta += "<ol>"
	for pag in base_datos:
		respuesta +=  "<li><a href='" + str(pag.id) +"'>" + pag.name + "</a>" + " " + pag.page 
	respuesta += "</ol>"
	return HttpResponse(respuesta)

def numero_pagina(request, num):
	try:
		page = Pages.objects.get(id = num)
		respuesta = page.page
	except Pages.DoesNotExist:
		respuesta = "Pagina no encontrada"
	return HttpResponse(respuesta)
