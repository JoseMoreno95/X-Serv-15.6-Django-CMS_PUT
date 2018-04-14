from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def mainPage(request):
    group = Pages.objects.all()
    list = ''
    for item in group:
        list = list + item.name + '<br>'
    return HttpResponse("La lista de recursos disponibles es la siguiente:<br><br>" +
    list + '<br>'
    "Un ejemplo de cómo pedir un recurso es: "
    "http://localhost:8000/pepito<br><br>"
    "Si pides un recurso que no existe, la página te lo indicará")

@csrf_exempt
def getPage(request, text):
    if request.method == "GET":
        try:
            object = Pages.objects.get(name = text)
            return HttpResponse(object.page)
        except Pages.DoesNotExist:
            return HttpResponse("No hay una página para " + text)
    else:
        page = Pages(name = text, page = request.body.decode("utf-8"))
        page.save()
        return HttpResponse("New page created")
