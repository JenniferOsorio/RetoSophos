from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crearHeroe/', views.crearHeroe),
    path('crearVillano/', views.crearVillano),
    path('crearPelea/', views.crearPelea),
    path('crearPatrocinador/', views.crearPatrocinador),
    path('gestionVillano/', views.gestion_villanos, name='gestion_villanos'),
    path('gestionPeleas/', views.gestion_pelea, name='gestion_pelea'),
    path('gestionPatrocinador/', views.gestion_patrocinador, name='gestion_patrocinador'),
    path('editarHeroe/<id_heroe>/', views.editarHeroe, name='editar_heroe'),
    path('editarVillano/<id_villano>/', views.editarVillano, name='editar_villano'),
    path('editarPelea/<id_pelea>/', views.editarPelea, name='editar_pelea'),
    path('editarPatrocinador/<id_patrocinador>/', views.editarPatrocinador, name='editar_patrocinador'),
    path('eliminarHeroe/<id_heroe>',views.eliminarHeroe, name='eliminar_heroe'),
    path('eliminarVillano/<int:id_villano>', views.eliminarVillano, name='eliminar_villano'),
    path('eliminarPelea/<id_pelea>',views.eliminarPelea, name='eliminar_pelea'),
    path('eliminarPatrocinador/<id_patrocinador>',views.eliminarPatrocinador, name='eliminar_patrocinador'),
    path('buscarHeroe/', views.buscarHeroe, name='buscarHeroe'),
    path('buscarVillano/', views.buscarVillano, name='buscarVillano'),
    path('buscarPelea/', views.buscarPelea, name='buscarPelea'),
    path('buscarPatrocinador/', views.buscarPatrocinador, name='buscarPatrocinador'),
]