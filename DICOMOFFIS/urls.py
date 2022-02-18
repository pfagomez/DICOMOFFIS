from django.urls import path, include
from django.shortcuts import redirect

from DICOMOFFIS import views

urlpatterns =[
   path("",views.home, name =("home")),
   path('home/' , lambda req: redirect('/')),
   path('allgemeines/', views.allgemeines, name= ('allgemeines')),
      path('allgemeines/dicom-einfuehrung', views.dicomeinfuehrung, name= ('dicom-einfuehrung')),
      path('allgemeines/standardisierung/', views.standardisierung, name=("standardisierung")),
   path('dcmtk/', views.dcmtk, name = ('dcmtk') ),
      path('dcmtk/dcmtk-einfuehrung', views.dcmtkeinfuehrung, name = ('dcmtk-einführung') ),
      path('dcmtk/softwareentwicklung_mit_dcmtk', views.softwareentwicklung-mit-dcmtk, name = ('softwareentwicklung mit dcmtk') ),
      path('dcmtk/dcmtk-tools', views.dcmtk-tools, name = ('dcmtk-tools') ),
      path('dcmtk/spenden', views.spenden, name = ('spenden') ),
      path('dcmtk/support', views.support, name = ('support') ),
   path('dcmtk-erweiterungsmodule/', views.dcmtkerweiterungsmodule, name=('dcmtk-erweiterungsmodule')),
      path('dcmtk-erweiterungsmodule/dcmjp2k', views.dcmjp2k, name=('dcmjp2k')),
      path('dcmtk-erweiterungsmodule/dcmppscu', views.dcmppscu, name=('dcmppscu')),
      path('dcmtk-erweiterungsmodule/dcmprint', views.dcmprint, name=('dcmprint')),
      path('dcmtk-erweiterungsmodule/dcmstcom', views.dcmstcom, name=('dcmstcom')),
      path('dcmtk-erweiterungsmodule/ppsmgr', views.ppsmgr, name=('ppsmgr')),
      path('dcmtk-erweiterungsmodule/testversionen', views.testversionen, name=('testversionen')),
      path('dcmtk-erweiterungsmodule/dcmpps', views.dcmpps, name=('dcmpps')),
   path('dicomscope/', views.dicomscope, name = ("dicomscope")),
   path('kontakt/', views.kontakt, name = ("kontakt")),
      path('kontakt/ansprechpartner', views.ansprechpartner, name = ("ansprechpartner")),
   path('dienstleistungen/', views.dienstleistungen, name = ("dienstleistungen")),
   path('dienstleistungen/dicom-beratung', views.dicomberatung, name = ("dicom-beratung")),
   path('dienstleistungen/dicom-schulung', views.dicomschulung, name = ("dicom-schulung")),
   path('dienstleistungen/ihe-schulung', views.iheschulung, name = ("ihe-schulung")),
   path('dienstleistungen/hl7-schulung', views.hl7schulung, name = ("hl7-schulung")),
   path('datenschutz/', views.datenschutz, name = ("datenschutz")),
   path('impressum/', views.impressum, name = ("impressum")),
]
