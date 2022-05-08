from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app/', views.app, name = 'app'), 
    path('plastic/', views.plastic, name = 'plastic page'),
    path('plastic_map/', views.plastic_map, name = 'plastic map page'),
    path('hartie/', views.hartie, name = 'foi page'),
    path('hartie_map/', views.hartie_map, name = 'foi map page '),
    path('mancare/', views.mancare, name = 'mancare page'),
    path('mancare_map/', views.mancare_map, name = 'mancare map page'),
    path('metale/', views.metale, name = 'metale page'),
    path('metale_map/', views.metale_map, name = 'metale map page'),
]