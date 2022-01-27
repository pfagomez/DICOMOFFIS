from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("Home")),
   path('Allgemeines/', views.allgemeines, name= ('Allgemeines')),
      path('Allgemeines/DICOM-Einführung', views.dicomEinführung, name= ('DICOM-Einführung')),
      path('Allgemeines/Standardisierung/', views.standardisierung, name=("Standardisierung")),
   path('DCMTK/', views.dcmtk, name = ('dcmtk') ),
      path('DCMTK/DCMTK-Einführung', views.dcmtkEinführung, name = ('DCMTK-Einführung') ),
      path('DCMTK/Softwareentwicklung mit DCMTK', views.softwareentwicklungMitDcmtk, name = ('Softwareentwicklung mit DCMTK') ),
      path('DCMTK/DCMTK-Tools', views.dcmtkTools, name = ('DCMTK-Tools') ),
      path('DCMTK/Spenden', views.spenden, name = ('Spenden') ),
      path('DCMTK/Support', views.support, name = ('Support') ),
   path('Home/' , lambda req: redirect('/')),
   path('DCMTK-Erweiterungsmodule/', views.dcmtkErweiterungsmodule, name=('DCMTK-Erweiterungsmodule')),
      path('DCMTK-Erweiterungsmodule/DCMJP2K', views.dcmjp2k, name=('DCMJP2K')),
      path('DCMTK-Erweiterungsmodule/DCMPPSCU', views.dcmppscu, name=('DCMPPSCU')),
      path('DCMTK-Erweiterungsmodule/DCMPRINT', views.dcmprint, name=('DCMPRINT')),
      path('DCMTK-Erweiterungsmodule/DCMPPSCU', views.dcmppscu, name=('DCMPPSCU')),
      path('DCMTK-Erweiterungsmodule/PPSMGR', views.ppsmgr, name=('PPSMGR')),
      path('DCMTK-Erweiterungsmodule/Testversionen', views.testversionen, name=('Testversionen')),
   path('DICOMscope/', views.dicomscope, name = ("DICOMscope")),
   path('Kontakt/', views.kontakt, name = ("Kontakt")),
      path('Kontakt/', views.kontakt, name = ("Kontakt")),
   path('Dienstleistungen/', views.dienstleistungen, name = ("Dienstleistungen")),
   path('Datenschutz/', views.datenschutz, name = ("Datenschutz")),
   path('Impressum/', views.impressum, name = ("Impressum")),

]
