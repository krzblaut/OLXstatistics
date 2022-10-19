from multiprocessing.spawn import import_main_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('krakow/', views.krakow, name='krakow'),
    path('katowice/', views.katowice, name='katowice'),
    path('gdansk/', views.gdansk, name='gdansk'),
    path('lodz/', views.lodz, name='lodz'),
    path('warszawa/', views.warszawa, name='warszawa'),
    path('rzeszow/', views.rzeszow, name='rzeszow'),
    path('kielce/', views.kielce, name='kielce'),
    path('szczecin/', views.szczecin, name='szczecin'),
    path('bydgoszcz/', views.bydgoszcz, name='bydgoszcz'),
    path('bialystok/', views.bialystok, name='bialystok'),
    path('lublin/', views.lublin, name='lublin'),
    path('wroclaw/', views.wroclaw, name='wroclaw'),

]