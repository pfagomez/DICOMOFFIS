from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("index2")),
   path('Allgemeines/', views.allgemeines, name= ('Allgemeines')),
   path('DCMTK/', views.dcmtk, name = ('dcmtk') ),
   path('Home/' , lambda req: redirect('/')),
   
]
