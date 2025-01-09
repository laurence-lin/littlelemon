from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("Home page of Restaurant APP")



def index(request):
    return render(request, 'index.html', {})

