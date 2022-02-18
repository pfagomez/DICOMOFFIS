from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, {'site': "home"}, name =("Home")),
   path('Allgemeines/', views.allgemeines, {'site': "Allgemeines"}, name= ('Allgemeines')),
      path('Allgemeines/DICOM-Einführung', views.dicomEinführung, {'site': "DICOM-Einführung"}, name= ('DICOM-Einführung')),
      path('Allgemeines/Standardisierung/', views.standardisierung,{'site': "Standardisierung"}, name=("Standardisierung")),
   path('DCMTK/', views.dcmtk, {'site': "dcmtk"}, name = ('dcmtk') ),
      path('DCMTK/DCMTK-Einführung', views.dcmtkEinführung, {'site': "DCMTK-Einführung"}, name = ('DCMTK-Einführung') ),
      path('DCMTK/Softwareentwicklung_mit_DCMTK', views.softwareentwicklungMitDcmtk, {'site': "Softwareentwicklung mit DCMTK"}, name = ('Softwareentwicklung mit DCMTK') ),
      path('DCMTK/DCMTK-Tools', views.dcmtkTools, {'site': "DCMTK-Tools"}, name = ('DCMTK-Tools') ),
      path('DCMTK/Spenden', views.spenden, {'site': "Spenden"}, name = ('Spenden') ),
      path('DCMTK/Support', views.support, {'site': "Support"}, name = ('Support') ),
   path('Home/' , lambda req: redirect('/')),
   path('DCMTK-Erweiterungsmodule/', views.dcmtkErweiterungsmodule, {'site': "DCMTK-Erweiterungsmodule"}, name=('DCMTK-Erweiterungsmodule')),
      path('DCMTK-Erweiterungsmodule/DCMJP2K', views.dcmjp2k, {'site': "DCMJP2K"}, name=('DCMJP2K')),
      path('DCMTK-Erweiterungsmodule/DCMPPSCU', views.dcmppscu, {'site': "DCMPPSCU"}, name=('DCMPPSCU')),
      path('DCMTK-Erweiterungsmodule/DCMPRINT', views.dcmprint, {'site': "DCMPRINT"}, name=('DCMPRINT')),
      path('DCMTK-Erweiterungsmodule/DCMSTCOM', views.dcmstcom, {'site': "DCMSTCOM"}, name=('DCMSTCOM')),
      path('DCMTK-Erweiterungsmodule/PPSMGR', views.ppsmgr, {'site': "PPSMGR"}, name=('PPSMGR')),
      path('DCMTK-Erweiterungsmodule/Testversionen', views.testversionen, {'site': "Testversionen"}, name=('Testversionen')),
      path('DCMTK-Erweiterungsmodule/DCMPPS', views.dcmpps, {'site': "DCMPPS"}, name=('DCMPPS')),
   path('DICOMscope/', views.dicomscope, {'site': "DICOMscope"}, name = ("DICOMscope")),
   path('Kontakt/', views.kontakt, {'site': "Kontakt"}, name = ("Kontakt")),
      path('Kontakt/Ansprechpartner', views.ansprechpartner, {'site': "Ansprechpartner"}, name = ("Ansprechpartner")),
   path('Dienstleistungen/', views.dienstleistungen, {'site': "Dienstleistungen"}, name = ("Dienstleistungen")),
   path('Dienstleistungen/DICOM-Beratung', views.dicomBeratung, {'site': "DICOM-Beratung"}, name = ("DICOM-Beratung")),
   path('Dienstleistungen/DICOM-Schulung', views.dicomSchulung, {'site': "DICOM-Schulung"}, name = ("DICOM-Schulung")),
   path('Dienstleistungen/IHE-Schulung', views.iheSchulung, {'site': "IHE-Schulung"}, name = ("IHE-Schulung")),
   path('Dienstleistungen/HL7-Schulung', views.hl7Schulung, {'site': "HL7-Schulung"}, name = ("HL7-Schulung")),
   path('Datenschutz/', views.datenschutz, {'site': "Datenschutz"}, name = ("Datenschutz")),
   path('Impressum/', views.impressum, {'site': "Impressum"}, name = ("Impressum")),
]
