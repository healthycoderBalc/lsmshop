from django.urls import path, include


from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# mercado pago
# from .views import (
#     PaymentCreateView,
#     PaymentFailureView,
#     PaymentPendingView,
#     PaymentSuccessView,
#     payment_webhook,
# )




app_name='polls'

urlpatterns = [
    #path('', views.index, name='index'),
    path('registrarse/', views.registro, name='registro'),
    path('errorRegistro/', views.errorRegistro, name='errorRegistro'),
    path('salir/', views.salir, name='salir'),
    path('ingresar/', views.entrar, name='entrar'),
    path('unauthorized/', views.noAutorizado, name='unauthorized'),
    path('perfilCliente', views.perfil, name="perfilCliente"),
    path('updateperfilCliente/', views.update_perfilCliente, name="updateperfilCliente"),
    path('updateperfilUser/', views.update_perfilUser, name="updateperfilCliente"),
    path('deletePerfil/', views.delete_perfil, name="deleteperfil"),
    path('', views.buscar, name='search_results'),
    path('listarClientes/', views.buscarCliente, name='search_resultsCliente'),
    path('negociosPorRubro/<id>', views.filtrarXRubros, name='filtrarXRubros'),
    path('seleccionHorarios/', views.seleccionHorarios, name='seleccionHorarios' ),
    path('negociosPorHorarios/<diaSemana>/<horaAbre>/<horaCierra>', views.filtrarXHorario, name='negociosPorHorarios' ),


    path('ingresar/', views.login_request, name='entrar'),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path('oauth/', include('social_django.urls', namespace='social')),

    path('', views.principal, name='principal'),
    path('creditos/', views.creditos, name='creditos'),
    
    #path('logout/', views.logout, name="user-logout"),
    path('loguincito/', views.loguincito, name="loguincito"),

    ##path('home/', TemplateView.as_view(template_name="home.html"), name="home"),

    # --------------------Cliente------------------------------------------- #
     path('cargarCliente/', views.cargarCliente, name='admCliente'),
     path('listarClientes/', views.listarClientes, name='admlCliente'),
     path('mostrarCliente/<id>', views.mostrarCliente, name='admmCliente'),
     path('updateCliente/<id>', views.update_cliente, name='admuCliente'),
     path('deleteCliente/<id>', views.delete_cliente, name='admdCliente'),

    # --------------------Suscripcion--------------------------------------- #
     path('cargarSuscripcion/', views.cargarSuscripcion, name='cargarSuscripcion'),
     path('listarSuscripciones/', views.listarSuscripciones, name='listarSuscripciones'),
     path('listarSuscripcionesAdmin/', views.administrarSuscripciones, name='administrarSuscripciones'),
     path('mostrarSuscripcion/<id>', views.mostrarSuscripcion, name='mostrarSuscripcion'),
     path('updateSuscripcion/<id>', views.update_suscripcion, name='update_suscripcion'),
     path('deleteSuscripcion/<id>', views.delete_suscripcion, name='delete_suscripcion'),

    # --------------------DiaSemana------------------------------------------- # 
     path('cargarDiaSemana/', views.cargarDiaSemana, name='cargarDiaSemana'),
     path('listarDiassemana/', views.listarDiasSemana, name='listarDiasSemana'),
     path('mostrarDiasemana/<id>', views.mostrarDiaSemana, name='mostrarDiaSemana'),
     path('updateDiasemana/<id>', views.update_diasemana, name='update_diasemana'),
     path('deleteDiasemana/<id>', views.delete_diasemana, name='delete_diasemana'),

    
    # --------------------Rubro------------------------------------------- #
     path('cargarRubro/', views.cargarRubro, name='cargarRubro'),
     path('listarRubros/', views.listarRubros, name='listarRubros'),
     path('mostrarRubro/<id>', views.mostrarRubro, name='mostrarRubro'),
     path('updateRubro/<id>', views.update_rubro, name='update_rubro'),
     path('deleteRubro/<id>', views.delete_rubro, name='delete_rubro'),
    
    # --------------------FormaContacto------------------------------------------- #
     path('cargarFormaContacto/', views.cargarFormaContacto, name='cargarFormaContacto'),
     path('listarFormascontacto/', views.listarFormasContacto, name='listarFormasContacto'),
     path('mostrarFormacontacto/<id>', views.mostrarFormaContacto, name='mostrarFormaContacto'),
     path('updateFormacontacto/<id>', views.update_formacontacto, name='update_formacontacto'),
     path('deleteFormacontacto/<id>', views.delete_formacontacto, name='delete_formacontacto'),

    # --------------------Negocio------------------------------------------- #
     path('cargarNegocio/', views.cargarNegocio, name='cargarNegocio'),
     path('suscripcionPaga/<id>', views.suscripcionPaga, name='suscripcionPaga'),
     path('listarNegocios/', views.listarNegocios, name='listarNegocios'),
     path('listarNegociosCliente/', views.administrarNegocios, name='administrarNegocios'),
     path('mostrarNegocio/<id>', views.mostrarNegocio, name='mostrarNegocio'),
     path('mostrarNegocioAdd/<id>', views.mostrarNegocioAdd, name='mostrarNegocioAdd'),
     path('updateNegocio/<id>', views.update_negocio, name='update_negocio'),
     path('deleteNegocio/<id>', views.delete_negocio, name='delete_negocio'),
     path('quitarSuscripciones/', views.downgradeBusinesses, name='quitarSuscripciones'),
    
    # --------------------NegocioHoraDia------------------------------------------- #
     path('cargarNegocioHoraDia/', views.cargarNegocioHoraDia, name='cargarNegocioHoraDia'),
     path('listarNegociohorariodias/', views.listarNegocioHorarioDias, name='listarNegocioHorarioDias'),
     path('mostrarNegociohorariodia/<id>', views.mostrarNegocioHorarioDia, name='mostrarNegocioHorarioDia'),
     path('updateNegociohorariodia/<id>', views.update_negociohorariodia, name='update_negociohorariodia'),
     path('deleteNegociohorariodia/<id>', views.delete_negociohorariodia, name='delete_negociohorariodia'),

    
    # --------------------NegocioRubro------------------------------------------- #
     path('cargarNegocioRubro/', views.cargarNegocioRubro, name='cargarNegocioRubro'),
     path('listarNegociorubros/', views.listarNegocioRubros, name='listarNegocioRubros'),
     path('mostrarNegociorubro/<id>', views.mostrarNegocioRubro, name='mostrarNegocioRubro'),
     path('updateNegociorubro/<id>', views.update_negociorubro, name='update_negociorubro'),
     path('deleteNegociorubro/<id>', views.delete_negociorubro, name='delete_negociorubro'),



    # --------------------NegocioFormaContacto------------------------------------------- #
     path('cargarNegocioFormaContacto/', views.cargarNegocioFormaContacto, name='cargarNegocioFormaContacto'),
     path('listarNegocioformacontactos/', views.listarNegocioFormaContacto, name='listarNegocioFormaContacto'),
     path('mostrarNegocioformacontacto/<id>', views.mostrarNegocioFormaContacto, name='mostrarNegocioFormaContacto'),
     path('updateNegocioformacontacto/<id>', views.update_negocioformacontacto, name='update_negocioformacontacto'),
     path('updateNegocioformacontactomodal/<id>', views.update_negocioformacontactomodal , name='update_negocioformacontactomodal'),
     path('deleteNegocioformacontacto/<id>', views.delete_negocioformacontacto, name='delete_negocioformacontacto'),



    # --------------------NegocioFormaContacto------------------------------------------- #


    path("process/<id>", views.pago, name="process"),
    path("failure/<id>", views.failure, name="failure"),
    path("pending/<id>", views.pending, name="pending"),
    path("success/<id>", views.success, name="success"),
    # path("webhook/", payment_webhook, name="webhook"),
 
]

