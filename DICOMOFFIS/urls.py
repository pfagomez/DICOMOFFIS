from django.urls import path, include
from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("index2")),
   path('Allgemeines.html/', views.allgemeines, name= ('Allgemeines')),
   path('DCMTK.html/', views.dcmtk, name = ('dcmtk') ),
   path('Home.html/' , views.home, name = ('home')),
]
