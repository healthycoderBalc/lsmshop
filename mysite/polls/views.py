
# Create your views here.
from re import L
from typing_extensions import Self
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .urls import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib import messages
from django.db.models import Q
from django.utils import dateparse
from django.db.models.functions import Lower

# ----------------------------------------------------------------------------------- #
# ---------------------------------Cliente------------------------------------------- #
# ----------------------------------------------------------------------------------- #

#from mysite.polls.models import Business
def cargarCliente(request):
    # dictionary for initial data with
    # field names as keys

    context ={}
 
    # add the dictionary during initialization
    if request.method == 'POST':
        form = ClientForm(request.POST or None, user = request.user)
        # form.fields["user"].queryset = User.objects.filter(user_id=usuario.id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mostrarCliente/'+ str(form.instance.pk))
    else:
        form = ClientForm(user = request.user)


    titulo = "Cliente"
    # context['usuario'] = usuario
    context['form']= form
    context["titulo"] = titulo     

    return render(request, "polls/cargar.html", context)


def listarClientes(request):
    context ={}
    
    if request.user.is_authenticated:

        if request.user.is_staff:
            titulo = "Cliente"
            # add the dictionary during initialization
            # context["dataset"] = Client.objects.all()
            context["dataset"] = Client.objects.order_by(Lower('user__first_name'))
            context["titulo"] = titulo
            direccion = "polls/cliente/listarclientes.html"
            print("staff")
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")
    
    return render(request, direccion , context)

def mostrarCliente(request, id):
    context ={}
 
    titulo = "Cliente"
    # add the dictionary during initialization
    context["data"] = Client.objects.get(id = id)
    context["titulo"] = titulo

         
    return render(request, "polls/cliente/mostrarcliente.html", context)

def update_cliente(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id = id)
 
    # pass the object as instance in form
    form = ClientForm(request.POST or None, instance = obj, user = request.user)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/perfilCliente")
 
    # add form dictionary to context
    titulo = "Cliente"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/cliente/updatecliente.html", context)


def delete_cliente(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/listarClientes/")
 
    titulo = "Cliente"
    context["titulo"] = titulo

    return render(request, "polls/cliente/deletecliente.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Suscripcion--------------------------------------- #
# ----------------------------------------------------------------------------------- #

def administrarSuscripciones(request):
    context={}

    # dataset = Business.objects.filter(cliente__id=id)
    if request.user.is_authenticated:

        if request.user.is_staff:
            dataset = Subscription.objects.all()


            titulo = "Suscripciones"


            # add the dictionary during initialization
            context["dataset"] = dataset

            context["titulo"] = titulo
            # context["clientecito"] = Client.objects.get(id = id)
            direccion = "polls/suscripcion/listarsuscripcionesadmin.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"


    return render(request, direccion, context)




def cargarSuscripcion(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

        if request.user.is_staff:
    # add the dictionary during initialization
            if request.method == 'POST':
                form = SubscriptionForm(request.POST or None)

                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/listarSuscripcionesAdmin/')
            else:
                form = SubscriptionForm()
                

            titulo = "Suscripcion"
            context['form']= form
            context["titulo"] = titulo
            direccion = "polls/cargar.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def listarSuscripciones(request):
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:

            titulo = "Suscripcion"
            # add the dictionary during initialization
            context["dataset"] = Subscription.objects.all()
            context["titulo"] = titulo
            direccion = "polls/suscripcion/listarsuscripciones.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)

def mostrarSuscripcion(request, id):
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
            titulo = "Suscripcion"
            # add the dictionary during initialization
            context["data"] = Subscription.objects.get(id = id)
            context["titulo"] = titulo
            direccion = "polls/suscripcion/mostrarsuscripcion.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)

def update_suscripcion(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(Subscription, id = id)
        
            # pass the object as instance in form
            form = SubscriptionForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/listarSuscripcionesAdmin/")
        
            # add form dictionary to context
            titulo = "Suscripcion"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/suscripcion/updatesuscripcion.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")
 
    return render(request, direccion, context)


def delete_suscripcion(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(Subscription, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarSuscripcionesAdmin/")
        
            titulo = "Suscripcion"
            context["titulo"] = titulo
            direccion = "polls/suscripcion/deletesuscripcion.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)








# ----------------------------------------------------------------------------------- #
# ---------------------------------DiaSemana----------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarDiaSemana(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # add the dictionary during initialization
            if request.method == 'POST':
                form = DayweekForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/mostrarDiasemana/'+ str(form.instance.pk))
            else:
                form = DayweekForm()
                

            titulo = "Dia Semana"
            context['form']= form
            context["titulo"] = titulo
            direccion = "polls/cargar.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def listarDiasSemana(request):
    context ={}
 

    titulo = "Dia Semana"
    # add the dictionary during initialization
    context["dataset"] = Dayweek.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/diasemana/listardiassemana.html", context)

def mostrarDiaSemana(request, id):
    context ={}
 
    titulo = "Dia Semana"
    # add the dictionary during initialization
    context["data"] = Dayweek.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls//diasemana/mostrardiasemana.html", context)

def update_diasemana(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

        if request.user.is_staff:

    # fetch the object related to passed id
            obj = get_object_or_404(Dayweek, id = id)
        
            # pass the object as instance in form
            form = DayweekForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarDiasemana/"+id)
        
            # add form dictionary to context
            titulo = "Dia Semana"
            context["form"] = form
            context["titulo"] = titulo

            direccion = "polls/diasemana/updatediasemana.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")
 
    return render(request, direccion, context)


def delete_diasemana(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(Dayweek, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarDiassemana/")
        
            titulo = "Dia Semana"
            context["titulo"] = titulo
            direccion = "polls/diasemana/deletediasemana.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Rubro--------------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # add the dictionary during initialization
            if request.method == 'POST':
                form = HeadingForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/mostrarRubro/'+ str(form.instance.pk))
            else:
                form = HeadingForm()
            
            titulo = "Rubro"
            context['form']= form
            context["titulo"] = titulo
            direccion = "polls/cargar.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def listarRubros(request):
    context ={}
 

    titulo = "Rubro"
    # add the dictionary during initialization
    context["dataset"] = Heading.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/rubro/listarrubros.html", context)

def mostrarRubro(request, id):
    context ={}
 
    titulo = "Rubro"
    # add the dictionary during initialization
    context["data"] = Heading.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/rubro/mostrarrubro.html", context)

def update_rubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(Heading, id = id)
        
            # pass the object as instance in form
            form = HeadingForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarRubro/"+id)
        
            # add form dictionary to context
            titulo = "Rubro"
            context["form"] = form
            context["titulo"] = titulo
 
            direccion = "polls/rubro/updaterubro.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def delete_rubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 

    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(Heading, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarRubros/")
        
            titulo = "Rubro"
            context["titulo"] = titulo

            direccion = "polls/rubro/deleterubro.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------FormaContacto------------------------------------- #
# ----------------------------------------------------------------------------------- #

def cargarFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # add the dictionary during initialization
            if request.method == 'POST':
                form = ContactFormForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/mostrarFormacontacto/'+ str(form.instance.pk))
            else:
                form = ContactFormForm()
            
            titulo = "Forma Contacto"
            context['form']= form
            context["titulo"] = titulo
            direccion = "polls/cargar.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")



    return render(request, direccion, context)


def listarFormasContacto(request):
    context ={}
 

    titulo = "Forma Contacto"
    # add the dictionary during initialization
    context["dataset"] = ContactForm.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/formacontacto/listarformascontacto.html", context)

def mostrarFormaContacto(request, id):
    context ={}
 
    titulo = "Forma Contacto"
    # add the dictionary during initialization
    context["data"] = ContactForm.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/formacontacto/mostrarformacontacto.html", context)

def update_formacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

        if request.user.is_staff:

    # fetch the object related to passed id
            obj = get_object_or_404(ContactForm, id = id)
        
            # pass the object as instance in form
            form = ContactFormForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarFormacontacto/"+id)
        
            # add form dictionary to context
            titulo = "Forma Contacto"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/formacontacto/updateformacontacto.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def delete_formacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    if request.user.is_authenticated:

        if request.user.is_staff:
    # fetch the object related to passed id
            obj = get_object_or_404(ContactForm, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarFormascontacto/")
        
            titulo = "Forma Contacto"
            context["titulo"] = titulo

            direccion = "polls/formacontacto/deleteformacontacto.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")



    return render(request, direccion, context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Negocio------------------------------------------- #
# ----------------------------------------------------------------------------------- #

def administrarNegocios(request):
    context={}

    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
    # dataset = Business.objects.filter(cliente__id=id)
        dataset = Business.objects.filter(cliente__id=cliente.id).order_by(Lower('nombre'))
        titulo = "Mis Negocios"
        # add the dictionary during initialization
        context["dataset"] = dataset
        context["titulo"] = titulo
        context["cliente"] = cliente
        # context["clientecito"] = Client.objects.get(id = id)
        direccion = "polls/negocio/listarnegocioscliente.html"
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def cargarNegocio(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # idN = None
    # add the dictionary during initialization
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BusinessForm(request.POST or None, request.FILES, user = request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/mostrarNegocioAdd/'+ str(form.instance.pk))
        else:
            form = BusinessForm(user = request.user)
            

        titulo = "Negocio"
        context['form']= form
        context["titulo"] = titulo
        direccion = "polls/negocio/cargarnegocio.html"
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def listarNegocios(request):
    context ={}
 

    titulo = "Negocio"
    # add the dictionary during initialization
    

    context["dataset"] = Business.objects.order_by('nombre')
    context["titulo"] = titulo
         
    return render(request, "polls/inicio.html", context)


def mostrarNegocio(request, id):
    context ={}
 
    titulo = "Negocio"

    rubros = BusinessArea.objects.filter(negocio__id=id)
    context["rubros"] = rubros 

    contactos = BusinessContactForm.objects.filter(negocio__id=id)
    context["contactos"] = contactos

    horarios = Businesshourday.objects.filter(negocio__id=id).order_by('diaSemana__id')
    context["horarios"] = horarios

    # add the dictionary during initialization
    context["data"] = Business.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/negocio/mostrarnegocio.html", context)

def mostrarNegocioAdd(request, id):
    context ={}

    

    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocio = Business.objects.get(id = id)
        if negocio.cliente == cliente:
            titulo = "Negocio"

            rubros = BusinessArea.objects.filter(negocio__id=id)
            context["rubros"] = rubros 

            contactos = BusinessContactForm.objects.filter(negocio__id=id)
            context["contactos"] = contactos

            horarios = Businesshourday.objects.filter(negocio__id=id).order_by('diaSemana__id')
            context["horarios"] = horarios

            # add the dictionary during initialization
            context["data"] = Business.objects.get(id = id)
            context["titulo"] = titulo
            direccion = "polls/negocio/mostrarnegocioadd.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")



    return render(request, direccion, context)


def update_negocio(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    

    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocio = Business.objects.get(id = id)
        if negocio.cliente == cliente:
    # fetch the object related to passed id
            obj = get_object_or_404(Business, id = id)
        
            # pass the object as instance in form
            form = BusinessForm(request.POST or None, instance = obj, user = request.user)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarNegocioAdd/"+id)
        
            # add form dictionary to context
            titulo = "Negocio"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/negocio/updatenegocio.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")
 
    return render(request, direccion, context)


def delete_negocio(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 

    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocio = Business.objects.get(id = id)
        if negocio.cliente == cliente:

            # fetch the object related to passed id
            obj = get_object_or_404(Business, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/")
        
            titulo = "Negocio"
            context["titulo"] = titulo
            direccion = "polls/negocio/deletenegocio.html"

        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)



# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioHoraDia------------------------------------ #
# ----------------------------------------------------------------------------------- #

def cargarNegocioHoraDia(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:

    # add the dictionary during initialization
        if request.method == 'POST':
            form = BusinesshourdayForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/mostrarNegociohorariodia/'+ str(form.instance.pk))
        else:
            form = BusinesshourdayForm()

        titulo = "Negocio Horario Dia"
        context['form']= form
        context["titulo"] = titulo
        direccion = "polls/cargar.html"

    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def listarNegocioHorarioDias(request):
    context ={}
 

    titulo = "Negocio Horario Dia"
    # add the dictionary during initialization
    context["dataset"] = Businesshourday.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/intermedio/listarnegociohorariodias.html", context)

def mostrarNegocioHorarioDia(request, id):
    context ={}
 
    titulo = "Negocio Horario Dia"
    # add the dictionary during initialization
    context["data"] = Businesshourday.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/intermedio/mostrarnegociohorariodia.html", context)

def update_negociohorariodia(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioHD = Businesshourday.objects.get(id = id)
        negocio = Business.objects.get(id = negocioHD.negocio.id)
        if negocio.cliente == cliente:
    # fetch the object related to passed id
            obj = get_object_or_404(Businesshourday, id = id)
        
            # pass the object as instance in form
            form = BusinesshourdayForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarNegocioAdd/"+str(Businesshourday.objects.get(id=id).negocio_id))
        
            # add form dictionary to context
            titulo = "Negocio Horario Dia"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/intermedio/updatenegociohorariodia.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def delete_negociohorariodia(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioHD = Businesshourday.objects.get(id = id)
        negocio = Business.objects.get(id = negocioHD.negocio.id)
        if negocio.cliente == cliente:
    # fetch the object related to passed id
            obj = get_object_or_404(Businesshourday, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarNegociohorariodias/")
        
            titulo = "Negocio Horario Dia"
            context["titulo"] = titulo
            direccion = "polls/intermedio/deletenegociohorariodia.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)



# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioRubro-------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarNegocioRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:
    # add the dictionary during initialization
        if request.method == 'POST':
            form = BusinessAreaForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/mostrarNegociorubro/'+ str(form.instance.pk))
        else:
            form = BusinessAreaForm()
        
        titulo = "Negocio Rubro"
        context['form']= form
        context["titulo"] = titulo
        direccion = "polls/cargar.html"
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def listarNegocioRubros(request):
    context ={}
 

    titulo = "Negocio Rubro"
    # add the dictionary during initialization
    context["dataset"] = BusinessArea.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/intermedio/listarnegociorubros.html", context)

def mostrarNegocioRubro(request, id):
    context ={}
 
    titulo = "Negocio Rubro"
    # add the dictionary during initialization
    context["data"] = BusinessArea.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/intermedio/mostrarnegociorubro.html", context)

def update_negociorubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioR = BusinessArea.objects.get(id = id)
        negocio = Business.objects.get(id = negocioR.negocio.id)
        if negocio.cliente == cliente:
    # fetch the object related to passed id
            obj = get_object_or_404(BusinessArea, id = id)
            
            # pass the object as instance in form
            form = BusinessAreaForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarNegociorubro/"+id)
        
            # add form dictionary to context
            titulo = "Negocio Rubro"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/intermedio/updatenegociorubro.html"
 
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)


def delete_negociorubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioR = BusinessArea.objects.get(id = id)
        negocio = Business.objects.get(id = negocioR.negocio.id)
        if negocio.cliente == cliente:

            # fetch the object related to passed id
            obj = get_object_or_404(BusinessArea, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarNegociorubros/")
        
            titulo = "Negocio Rubro"
            context["titulo"] = titulo
            direccion = "polls/intermedio/deletenegociorubro.html"
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioFormaContacto------------------------------ #
# ----------------------------------------------------------------------------------- #

def cargarNegocioFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    if request.user.is_authenticated:
    # add the dictionary during initialization
        if request.method == 'POST':
            form = BusinessContactFormForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/mostrarNegocioformacontacto/'+ str(form.instance.pk))
        else:
            form = BusinessContactFormForm()
        

        titulo = "Negocio Forma Contacto"
        context['form']= form
        context["titulo"] = titulo
        direccion = "polls/cargar.html"
    
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)


def listarNegocioFormaContacto(request):
    context ={}
 

    titulo = "Negocio Forma Contacto"
    # add the dictionary during initialization
    context["dataset"] = BusinessContactForm.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/intermedio/listarnegocioformacontactos.html", context)

def mostrarNegocioFormaContacto(request, id):
    context ={}
 
    titulo = "Negocio Forma Contacto"
    # add the dictionary during initialization
    context["data"] = BusinessContactForm.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/intermedio/mostrarnegocioformacontacto.html", context)

def update_negocioformacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioFC = BusinessContactForm.objects.get(id = id)
        negocio = Business.objects.get(id = negocioFC.negocio.id)
        if negocio.cliente == cliente:
    # fetch the object related to passed id
            obj = get_object_or_404(BusinessContactForm, id = id)
        
            # pass the object as instance in form
            form = BusinessContactFormForm(request.POST or None, instance = obj)
        
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/mostrarNegocioAdd/"+ str(BusinessContactForm.objects.get(id = id).negocio_id) )
                # return HttpResponseRedirect("/mostrarNegocioformacontacto/"+id)
        
            # add form dictionary to context
            titulo = "Negocio Forma Contacto"
            context["form"] = form
            context["titulo"] = titulo
            direccion = "polls/intermedio/updatenegocioformacontacto.html"
 
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)



# Esta funcion nunca la use
def update_negocioformacontactomodal(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(BusinessContactForm, id = id)
 
    # pass the object as instance in form
    form = BusinessContactFormForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mostrarNegocioformacontacto/"+id)
 
    # add form dictionary to context
    titulo = "Negocio Forma Contacto"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/intermedio/updatenegocioformacontactomodal.html", context)




def delete_negocioformacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    
    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)
        negocioFC = BusinessContactForm.objects.get(id = id)
        negocio = Business.objects.get(id = negocioFC.negocio.id)
        if negocio.cliente == cliente:
            # fetch the object related to passed id
            obj = get_object_or_404(Dayweek, id = id)
        
        
            if request.method =="POST":
                # delete object
                obj.delete()
                # after deleting redirect to
                # home page
                return HttpResponseRedirect("/listarNegocioformacontactos/")
        
            titulo = "Negocio Forma Contacto"
            context["titulo"] = titulo
            direccion = "polls/intermedio/deletenegocioformacontacto.html"
 
        else:
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no user")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")



    return render(request, direccion, context)












def principal(request):

    context ={}
    titulo = "LSM Shop"
    context["titulo"] = titulo
    context["negocios"] = Business.objects.order_by(Lower('nombre'))
    context["categorias"] = Heading.objects.all()

    return render(request, "polls/inicio.html", context)


def creditos(request):
    context ={}
    return render(request, "polls/creditos.html", context)



# Esta funcion no se usa
def loguincito(request):
    return render(request, "polls/login.html")





from django.views.generic import TemplateView

# Esta funcion se usa?
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 




# ----------------------------------------------------------------------------------- #
# ---------------------------------Autenticacion------------------------------------- #
# ----------------------------------------------------------------------------------- #

def registro(request):

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada : {nombre_usuario}")
            login(request, usuario)
            # backend='django.contrib.auth.backends.ModelBackend'
            return redirect("polls:admCliente")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")

    form = RegistroForm()
    return render(request, "polls/registrarse.html", {"form": form})

def salir(request):
    logout(request)
    return redirect("polls:principal")

def entrar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                return redirect("polls:principal")
            else:
                messages.error(request, "Usuario o contraseña incorrecta")
        else:
          messages.error(request, "Usuario o contraseña incorrecta")  

    form = AuthenticationForm()
    return render(request, "polls/entrar.html", {"form": form})


def login_request(request):
    login(request)
    return render(request, "polls/entrar.html")

# ---------------------------------Perfil del logueado------------------------------- #


def perfil(request):
    context = {}

    if request.user.is_authenticated:
        cliente = Client.objects.get(user__pk = request.user.id)

        context["cliente"] = cliente
        direccion = "polls/perfilcliente.html"
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")

    return render(request, direccion, context)

# -----------------------------
# Revisar estas dos funciones que siguen
# -----------------------------
def update_perfilCliente(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, user__pk = request.user.id)
 
    # pass the object as instance in form
    form = ClientForm(request.POST or None, instance = obj, user = request.user)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/updateperfilUser")
 
    # add form dictionary to context
    titulo = "Cliente"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updateperfilCliente.html", context)

def update_perfilUser(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, pk = request.user.id)
 
    # pass the object as instance in form
    form = PerfilForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        print("valido")
        return HttpResponseRedirect("/perfilCliente")
    else:
        print("No valido")
 
    # add form dictionary to context
    titulo = "Cliente"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updateperfilUser.html", context)



# ---------------------------------Unauthorized-------------------------------------- #

def noAutorizado(request):
    context = {}
    return render(request, "polls/unauthorized.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Busqueda------------------------------------------ #
# ----------------------------------------------------------------------------------- #


# ---------------------------------Por negocio--------------------------------------- #
def buscar(request):
    context = {}
    negocios = []
    categorias = Heading.objects.all()
    if request.method == "GET":
        query = request.GET.get('q', None)
        if query:
            negocios = Business.objects.filter(
                Q(nombre__icontains=query)
            ).order_by(Lower('nombre'))
        else:
            negocios = Business.objects.order_by(Lower('nombre'))
    print(negocios)
    print(query)
    context["negocios"] = negocios
    context["query"] = query
    context["categorias"] = categorias

    return render(request, "polls/inicio.html", context)


# ---------------------------------Por rubro------------------------------------------ #
def filtrarXRubros(request, id):
    context = {}
    categorias = Heading.objects.all()
    rubro = Heading.objects.get(id = id)
    negocios = Business.objects.filter(rubros__id=id).order_by(Lower('nombre'))

    context["negocios"] = negocios
    context["rubro"] = rubro
    context["categorias"] = categorias
    #direccion = "polls/busqueda/filtrarrubros.html"
    direccion = "polls/inicio.html"

    return render(request, direccion , context)


# ---------------------------------Por dia y horario--------------------------------------- #
def seleccionHorarios(request):
    context = {}

    if request.method == 'POST': # If the form has been submitted...
        form = DateRangeForm(request.POST or None) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            dia = form.cleaned_data.get('dia')
            # dia1 = dia.strftime('%H:%M:%S')
            horaAbre = form.cleaned_data.get('start_date')
            horaAbre1 = horaAbre.strftime('%H:%M:%S')
            horaCierra = form.cleaned_data.get('end_date')
            horaCierra1 = horaCierra.strftime('%H:%M:%S')

            return HttpResponseRedirect('/negociosPorHorarios/'+ dia.dia +'/'+horaAbre1+'/'+horaCierra1) # Redirect after POST
    else:
        form = DateRangeForm() # An unbound form
    
    context['form']= form

    return render(request, "polls/busqueda/seleccionhorarios.html", context)

def filtrarXHorario(request, diaSemana, horaAbre, horaCierra):
    context = {}
    categorias = Heading.objects.all()
    negociosDia = Businesshourday.objects.filter(diaSemana__dia = diaSemana)
    # for neg in negociosDia:
    #     print(neg.negocio.nombre)
    #     print("por Dia")

    negociosHorario = negociosDia.filter(horaAbre__lte=horaAbre, horaCierra__gte=horaCierra).order_by(Lower('negocio__nombre'))
    
    negocios = []
    for negH in negociosHorario:
        for neg in Business.objects.all():
            if negH.negocio == neg:
                negocios.append(neg)

    
    # for neg in negociosHorario:
    #     print("negocito")
    #     print(neg.negocio.nombre)

    # print(negociosHorario[0])

    context["dia"] = diaSemana
    context["horaAbre"] = horaAbre
    context["horaCierra"] = horaCierra
    context["dataset"] = negociosHorario
    context["negociosD"] = negociosDia
    context["negocios"] = negocios
    context["categorias"] = categorias


    # direccion = "polls/busqueda/filtrarhorarios.html"
    direccion = "polls/inicio.html"

    return render(request, direccion, context)


    # ---------------------------------Buscar cliente--------------------------------------- #

def buscarCliente(request):
    context = {}

    if request.user.is_authenticated:
        if request.user.is_staff:
            clientes = []
            if request.method == "GET":
                query = request.GET.get('q', None)
                if query:
                    clientes = Client.objects.filter(
                        # Q(telefono__icontains=query)
                        Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) |Q(user__username__icontains=query)
                    ).order_by(Lower('user__last_name'))
                else:
                    clientes = Client.objects.order_by(Lower('user__last_name'))
            print("clientes" + str(clientes))
            print(query)
            context["dataset"] = clientes
            context["query"] = query
            direccion = "polls/cliente/listarClientes.html"
        else: 
            context["titulo"] = "No autorizado"
            direccion = "polls/unauthorized.html"
            print("no staff")
    else:
        context["titulo"] = "No autorizado"
        direccion = "polls/unauthorized.html"
        print("no user")


    return render(request, direccion, context)