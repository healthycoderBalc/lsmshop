
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .urls import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# ----------------------------------------------------------------------------------- #
# ---------------------------------Cliente------------------------------------------- #
# ----------------------------------------------------------------------------------- #

#from mysite.polls.models import Business
def cargarCliente(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()

    titulo = "Cliente"
    context['form']= form
    context["titulo"] = titulo     

    return render(request, "polls/cargar.html", context)

def listarClientes(request):
    context ={}
 

    titulo = "Cliente"
    # add the dictionary during initialization
    context["dataset"] = Client.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarclientes.html", context)

def mostrarCliente(request, id):
    context ={}
 
    titulo = "Cliente"
    # add the dictionary during initialization
    context["data"] = Client.objects.get(id = id)
    context["titulo"] = titulo

         
    return render(request, "polls/mostrarcliente.html", context)

def update_cliente(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id = id)
 
    # pass the object as instance in form
    form = ClientForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mostrarCliente/"+id)
 
    # add form dictionary to context
    titulo = "Cliente"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updatecliente.html", context)


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

    return render(request, "polls/deletecliente.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Suscripcion--------------------------------------- #
# ----------------------------------------------------------------------------------- #

def cargarSuscripcion(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
         

    titulo = "Suscripcion"
    context['form']= form
    context["titulo"] = titulo  


    return render(request, "polls/cargar.html", context)


def listarSuscripciones(request):
    context ={}
 

    titulo = "Suscripcion"
    # add the dictionary during initialization
    context["dataset"] = Subscription.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarsuscripciones.html", context)

def mostrarSuscripcion(request, id):
    context ={}
 
    titulo = "Suscripcion"
    # add the dictionary during initialization
    context["data"] = Subscription.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarsuscripcion.html", context)

def update_suscripcion(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Subscription, id = id)
 
    # pass the object as instance in form
    form = SubscriptionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mostrarSuscripcion/"+id)
 
    # add form dictionary to context
    titulo = "Suscripcion"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updatesuscripcion.html", context)


def delete_suscripcion(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Subscription, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/listarSuscripciones/")
 
    titulo = "Suscripcion"
    context["titulo"] = titulo

    return render(request, "polls/deletesuscripcion.html", context)








# ----------------------------------------------------------------------------------- #
# ---------------------------------DiaSemana----------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarDiaSemana(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = DayweekForm(request.POST or None)
    if form.is_valid():
        form.save()
         

    titulo = "Dia Semana"
    context['form']= form
    context["titulo"] = titulo

    return render(request, "polls/cargar.html", context)


def listarDiasSemana(request):
    context ={}
 

    titulo = "Dia Semana"
    # add the dictionary during initialization
    context["dataset"] = Dayweek.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listardiassemana.html", context)

def mostrarDiaSemana(request, id):
    context ={}
 
    titulo = "Dia Semana"
    # add the dictionary during initialization
    context["data"] = Dayweek.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrardiasemana.html", context)

def update_diasemana(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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
 
    return render(request, "polls/updatediasemana.html", context)


def delete_diasemana(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deletediasemana.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Rubro--------------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = HeadingForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    titulo = "Rubro"
    context['form']= form
    context["titulo"] = titulo


    return render(request, "polls/cargar.html", context)


def listarRubros(request):
    context ={}
 

    titulo = "Rubro"
    # add the dictionary during initialization
    context["dataset"] = Heading.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarrubros.html", context)

def mostrarRubro(request, id):
    context ={}
 
    titulo = "Rubro"
    # add the dictionary during initialization
    context["data"] = Heading.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarrubro.html", context)

def update_rubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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
 
    return render(request, "polls/updaterubro.html", context)


def delete_rubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deleterubro.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------FormaContacto------------------------------------- #
# ----------------------------------------------------------------------------------- #

def cargarFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ContactFormForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    titulo = "Forma Contacto"

    context['form']= form
    context["titulo"] = titulo

    return render(request, "polls/cargar.html", context)


def listarFormasContacto(request):
    context ={}
 

    titulo = "Forma Contacto"
    # add the dictionary during initialization
    context["dataset"] = ContactForm.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarformascontacto.html", context)

def mostrarFormaContacto(request, id):
    context ={}
 
    titulo = "Forma Contacto"
    # add the dictionary during initialization
    context["data"] = ContactForm.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarformacontacto.html", context)

def update_formacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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
 
    return render(request, "polls/updateformacontacto.html", context)


def delete_formacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deleteformacontacto.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Negocio------------------------------------------- #
# ----------------------------------------------------------------------------------- #

def cargarNegocio(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    if request.method == 'POST':
        form = BusinessForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:principal')
    else:
        form = BusinessForm()
         

    titulo = "Negocio"
    context['form']= form
    context["titulo"] = titulo

    return render(request, "polls/cargar.html", context)


def listarNegocios(request):
    context ={}
 

    titulo = "Negocio"
    # add the dictionary during initialization
    

    context["dataset"] = Business.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/inicio.html", context)

def mostrarNegocio(request, id):
    context ={}
 
    titulo = "Negocio"

    rubros = BusinessArea.objects.filter(negocio__id=id)
    context["rubros"] = rubros 

    contactos = BusinessContactForm.objects.filter(negocio__id=id)
    context["contactos"] = contactos

    horarios = Businesshourday.objects.filter(negocio__id=id)
    context["horarios"] = horarios

    # add the dictionary during initialization
    context["data"] = Business.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarnegocio.html", context)

def update_negocio(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Business, id = id)
 
    # pass the object as instance in form
    form = BusinessForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mostrarNegocio/"+id)
 
    # add form dictionary to context
    titulo = "Negocio"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updatenegocio.html", context)


def delete_negocio(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Business, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/listarNegocios/")
 
    titulo = "Negocio"
    context["titulo"] = titulo

    return render(request, "polls/deletenegocio.html", context)



# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioHoraDia------------------------------------ #
# ----------------------------------------------------------------------------------- #

def cargarNegocioHoraDia(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinesshourdayForm(request.POST or None)
    if form.is_valid():
        form.save()
         

    titulo = "Negocio Horario Dia"
    context['form']= form
    context["titulo"] = titulo

    
    return render(request, "polls/cargar.html", context)


def listarNegocioHorarioDias(request):
    context ={}
 

    titulo = "Negocio Horario Dia"
    # add the dictionary during initialization
    context["dataset"] = Businesshourday.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarnegociohorariodias.html", context)

def mostrarNegocioHorarioDia(request, id):
    context ={}
 
    titulo = "Negocio Horario Dia"
    # add the dictionary during initialization
    context["data"] = Businesshourday.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarnegociohorariodia.html", context)

def update_negociohorariodia(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Businesshourday, id = id)
 
    # pass the object as instance in form
    form = BusinesshourdayForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mostrarNegociohorariodia/"+id)
 
    # add form dictionary to context
    titulo = "Negocio Horario Dia"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updatenegociohorariodia.html", context)


def delete_negociohorariodia(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deletenegociohorariodia.html", context)



# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioRubro-------------------------------------- #
# ----------------------------------------------------------------------------------- #


def cargarNegocioRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinessAreaForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    titulo = "Negocio Rubro"
    context['form']= form
    context["titulo"] = titulo

    return render(request, "polls/cargar.html", context)


def listarNegocioRubros(request):
    context ={}
 

    titulo = "Negocio Rubro"
    # add the dictionary during initialization
    context["dataset"] = BusinessArea.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarnegociorubros.html", context)

def mostrarNegocioRubro(request, id):
    context ={}
 
    titulo = "Negocio Rubro"
    # add the dictionary during initialization
    context["data"] = BusinessArea.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarnegociorubro.html", context)

def update_negociorubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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
 
    return render(request, "polls/updatenegociorubro.html", context)


def delete_negociorubro(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deletenegociorubro.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------NegocioFormaContacto------------------------------ #
# ----------------------------------------------------------------------------------- #

def cargarNegocioFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinessContactFormForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    titulo = "Negocio Forma Contacto"
    context['form']= form
    context["titulo"] = titulo


    return render(request, "polls/cargar.html", context)


def listarNegocioFormaContacto(request):
    context ={}
 

    titulo = "Negocio Forma Contacto"
    # add the dictionary during initialization
    context["dataset"] = BusinessContactForm.objects.all()
    context["titulo"] = titulo
         
    return render(request, "polls/listarnegocioformacontactos.html", context)

def mostrarNegocioFormaContacto(request, id):
    context ={}
 
    titulo = "Negocio Forma Contacto"
    # add the dictionary during initialization
    context["data"] = BusinessContactForm.objects.get(id = id)
    context["titulo"] = titulo

    return render(request, "polls/mostrarnegocioformacontacto.html", context)

def update_negocioformacontacto(request, id):
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
 
    return render(request, "polls/updatenegocioformacontacto.html", context)


def delete_negocioformacontacto(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
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

    return render(request, "polls/deletenegocioformacontacto.html", context)












def principal(request):

    context ={}
    titulo = "LSM Shop"
    context["titulo"] = titulo
    context["negocios"] = Business.objects.all

    return render(request, "polls/inicio.html", context)

def login(request):

    return render(request, "polls/login.html")


def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("polls:principal")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request, "polls/signup.html", {"form": form})

def logout(request):
    logout(request)
    return redirect('/')

def loguincito(request):
    return render(request, "polls/home.html")





from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 