from django.shortcuts import render
from DICOMOFFIS import views

# Create your views here.
def index2 (request):
    return render (request,'Website/index2.html');