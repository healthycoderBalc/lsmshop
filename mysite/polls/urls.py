from django.urls import path, include


from . import views
from django.views.generic import TemplateView




app_name='polls'

urlpatterns = [
    #path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('', views.principal, name='principal'),
    path('signup/', views.signup, name='signup'),
    #path('logout/', views.logout, name="user-logout"),
    path('loguincito/', views.loguincito, name="loguincito"),

    ##path('home/', TemplateView.as_view(template_name="home.html"), name="home"),

     path('cargarCliente/', views.cargarCliente, name='admCliente'),
     path('cargarSuscripcion/', views.cargarSuscripcion, name='cargarSuscripcion'),
     path('cargarDiaSemana/', views.cargarDiaSemana, name='cargarDiaSemana'),
     path('cargarRubro/', views.cargarRubro, name='cargarRubro'),
     path('cargarFormaContacto/', views.cargarFormaContacto, name='cargarFormaContacto'),
     path('cargarNegocio/', views.cargarNegocio, name='cargarNegocio'),
     path('cargarNegocioHoraDia/', views.cargarNegocioHoraDia, name='cargarNegocioHoraDia'),
     path('cargarNegocioRubro/', views.cargarNegocioRubro, name='cargarNegocioRubro'),
     path('cargarNegocioFormaContacto/', views.cargarNegocioFormaContacto, name='cargarNegocioFormaContacto'),
     
     
     

 
]