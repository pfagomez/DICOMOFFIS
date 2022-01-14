from django.urls import path, include
from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("index2")),
   path('Allgemeines/', views.allgemeines, name= ('Allgemeines')),
   path('DCMTK/', views.dcmtk, name = ('dcmtk') ),
   path('Home/' , views.home, name = ('home')),
]
