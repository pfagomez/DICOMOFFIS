from django.urls import path
from DICOMOFFIS import views

urlpatterns =[
   path("",views.index2, name =("index2"))
]
