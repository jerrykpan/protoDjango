from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpReponse("Hello, world. You're at the polls index.")