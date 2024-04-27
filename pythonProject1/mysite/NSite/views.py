from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'NSite/site.html')
def IT(request):
    return render(request, 'NSite/pj1.html')

def VR_AR(request):
    return render(request, 'NSite/pj2.html')

def Autokvantum(request):
    return render(request, 'NSite/pj3.html')

def Airkvantum(request):
    return render(request, 'NSite/pj4.html')

def Hitech(request):
    return render(request, 'NSite/pj5.html')

def Promdisain(request):
    return render(request, 'NSite/pj6.html')

def Prompobokvantum(request):
    return render(request, 'NSite/pj7.html')
def VR_Vistavka(request):
    return render(request, 'NSite/index.html')


