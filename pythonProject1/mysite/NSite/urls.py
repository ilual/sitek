from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('IT', views.IT, name='pj1'),
    path('VR_AR', views.VR_AR, name='pj2'),
    path('Autokvantum', views.Autokvantum, name='pj3'),
    path('Airkvantum', views.Airkvantum, name='pj4'),
    path('Hitech', views.Hitech, name='pj5'),
    path('Promdisain', views.Promdisain, name='pj6'),
    path('Prompobokvantum', views.Prompobokvantum, name='pj7'),
    path('VR_Vistavka', views.VR_Vistavka, name='index'),
]
