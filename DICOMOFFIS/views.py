from django.shortcuts import render

# Create your views here.
def index2 (request):
    return render (request,'Website/index2.html');

def allgemeines (request):
    return render (request,'Website/Allgemeines.html')

def dcmtk (request):
    return render (request, 'Website/DCMTK.html')

def home (request):
    return render (request, 'Website/Home.html')

def dcmtkErweiterungsmodule (request):
    return render (request, 'Website/DCMTK-Erweiterungsmodule.html')

def dicomscope (request):
    return render(request, 'Website/DICOMscope.html')

def kontakt (request):
    return render(request, 'Website/Kontakt.html')

def dienstleistungen (request):
    return render(request, 'Website/Dienstleistungen.html')

def datenschutz (request):
    return render(request, 'Website/Datenschutz.html')

def impressum (request):
    return render(request, 'Website/Impressum.html')