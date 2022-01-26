from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("Home")),
   path('Allgemeines/', views.allgemeines, name= ('Allgemeines')),
   path('DCMTK/', views.dcmtk, name = ('dcmtk') ),
   path('Home/' , lambda req: redirect('/')),
   path('DCMTK-Erweiterungsmodule/', views.dcmtkErweiterungsmodule, name=('DCMTK-Erweiterungsmodule')),
   path('DICOMscope/', views.dicomscope, name = ("DICOMscope")),
   path('Kontakt/', views.kontakt, name = ("Kontakt")),
   path('Dienstleistungen/', views.dienstleistungen, name = ("Dienstleistungen")),
   path('Datenschutz/', views.datenschutz, name = ("Datenschutz")),
   path('Impressum/', views.impressum, name = ("Impressum")),
   path('Allgemeines/Standardisierung/', views.standardisierung, name=("Standardisierung")),

]
