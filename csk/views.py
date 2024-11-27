from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1> Ruturaj is a Captain </h1>")
def viceCaptain(request):
    return HttpResponse("<h2>jadeja is vice Captain</h2>")

