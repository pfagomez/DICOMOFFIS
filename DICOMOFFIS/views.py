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