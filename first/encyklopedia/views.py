from django.http import HttpResponse
from django.shortcuts import loader

from .models import Nation, Tank, Type
# Create your views here.

def index(request):
    return HttpResponse("Great vevicle almanach")
    
def nation(request):
    nation_list = Nation.objects.all()
    template = loader.get_template('encyklopedia/nations.html')
    context = {'nation_list': nation_list}
    return HttpResponse(template.render (context, request))

def tanks(request):
    tanks_list = Tank.objects.all()
    template = loader.get_template('encyklopedia/tanks.html')
    context = {'tanks_list': tanks_list}
    return HttpResponse(template.render (context, request))

def types(request):
    types_list = Type.objects.all()
    template = loader.get_template('encyklopedia/types.html')
    context = {'types_list': types_list}
    return HttpResponse(template.render (context, request))