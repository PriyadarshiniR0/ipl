from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def captain(response):
    return HttpResponse('<h1>Virat is a captain</h1>')
