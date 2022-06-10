from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the encyklopedia index.")
def detail(request, nation_id):
    return HttpResponse("You are looking at Nation %s" %request)
