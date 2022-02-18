from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("Home")),
   path('Allgemeines/', views.allgemeines, name= ('Allgemeines')),
      path('Allgemeines/DICOM-Einführung', views.dicomEinführung, name= ('DICOM-Einführung')),
      path('Allgemeines/Standardisierung/', views.standardisierung,{'site': "Standardisierung"}, name=("Standardisierung")),
   path('DCMTK/', views.dcmtk, name = ('dcmtk') ),
      path('DCMTK/DCMTK-Einführung', views.dcmtkEinführung, name = ('DCMTK-Einführung') ),
      path('DCMTK/Softwareentwicklung_mit_DCMTK', views.softwareentwicklungMitDcmtk, name = ('Softwareentwicklung mit DCMTK') ),
      path('DCMTK/DCMTK-Tools', views.dcmtkTools, name = ('DCMTK-Tools') ),
      path('DCMTK/Spenden', views.spenden, name = ('Spenden') ),
      path('DCMTK/Support', views.support, name = ('Support') ),
   path('Home/' , lambda req: redirect('/')),
   path('DCMTK-Erweiterungsmodule/', views.dcmtkErweiterungsmodule, name=('DCMTK-Erweiterungsmodule')),
      path('DCMTK-Erweiterungsmodule/DCMJP2K', views.dcmjp2k, name=('DCMJP2K')),
      path('DCMTK-Erweiterungsmodule/DCMPPSCU', views.dcmppscu, name=('DCMPPSCU')),
      path('DCMTK-Erweiterungsmodule/DCMPRINT', views.dcmprint, name=('DCMPRINT')),
      path('DCMTK-Erweiterungsmodule/DCMSTCOM', views.dcmstcom, name=('DCMSTCOM')),
      path('DCMTK-Erweiterungsmodule/PPSMGR', views.ppsmgr, name=('PPSMGR')),
      path('DCMTK-Erweiterungsmodule/Testversionen', views.testversionen, name=('Testversionen')),
      path('DCMTK-Erweiterungsmodule/DCMPPS', views.dcmpps, name=('DCMPPS')),
   path('DICOMscope/', views.dicomscope, name = ("DICOMscope")),
   path('Kontakt/', views.kontakt, name = ("Kontakt")),
      path('Kontakt/Ansprechpartner', views.ansprechpartner, name = ("Ansprechpartner")),
   path('Dienstleistungen/', views.dienstleistungen, name = ("Dienstleistungen")),
   path('Dienstleistungen/DICOM-Beratung', views.dicomBeratung, name = ("DICOM-Beratung")),
   path('Dienstleistungen/DICOM-Schulung', views.dicomSchulung, name = ("DICOM-Schulung")),
   path('Dienstleistungen/IHE-Schulung', views.iheSchulung, name = ("IHE-Schulung")),
   path('Dienstleistungen/HL7-Schulung', views.hl7Schulung, name = ("HL7-Schulung")),
   path('Datenschutz/', views.datenschutz, name = ("Datenschutz")),
   path('Impressum/', views.impressum, name = ("Impressum")),
]
