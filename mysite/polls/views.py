
# Create your views here.
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

def administrarNegocios(request):
    context={}

    cliente = Client.objects.get(user__pk = request.user.id)
    # dataset = Business.objects.filter(cliente__id=id)
    dataset = Business.objects.filter(cliente__id=cliente.id)


    titulo = "Mis Negocios"


    # add the dictionary during initialization
    context["dataset"] = dataset

    context["titulo"] = titulo
    context["cliente"] = cliente
    # context["clientecito"] = Client.objects.get(id = id)

    return render(request, "polls/listarnegocioscliente.html", context)


def cargarNegocio(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # idN = None
    # add the dictionary during initialization
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

    return render(request, "polls/cargarnegocio.html", context)


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

def mostrarNegocioAdd(request, id):
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

    return render(request, "polls/mostrarnegocioadd.html", context)


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
        return HttpResponseRedirect("/mostrarNegocioAdd/"+id)
 
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
        return HttpResponseRedirect("/mostrarNegocioAdd/"+str(Businesshourday.objects.get(id=id).negocio_id))
 
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
        return HttpResponseRedirect("/mostrarNegocioAdd/"+ str(BusinessContactForm.objects.get(id = id).negocio_id) )
        # return HttpResponseRedirect("/mostrarNegocioformacontacto/"+id)
 
    # add form dictionary to context
    titulo = "Negocio Forma Contacto"
    context["form"] = form
    context["titulo"] = titulo
 
    return render(request, "polls/updatenegocioformacontacto.html", context)


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
 
    return render(request, "polls/updatenegocioformacontactomodal.html", context)




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
    context["categorias"] = Heading.objects.all

    return render(request, "polls/inicio.html", context)






def loguincito(request):
    return render(request, "polls/home.html")





from django.views.generic import TemplateView


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
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
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


def perfil(request):
    context = {}

    cliente = Client.objects.get(user__pk = request.user.id)

    context["cliente"] = cliente

    return render(request, "polls/perfilcliente.html", context)


# ----------------------------------------------------------------------------------- #
# ---------------------------------Busqueda------------------------------------------ #
# ----------------------------------------------------------------------------------- #
def buscar(request):
    context = {}
    negocios = []
    categorias = Heading.objects.all()
    if request.method == "GET":
        query = request.GET.get('q', None)
        if query:
            negocios = Business.objects.filter(
                Q(nombre__icontains=query)
            )
        else:
            negocios = Business.objects.all()
    print(negocios)
    print(query)
    context["negocios"] = negocios
    context["query"] = query
    context["categorias"] = categorias

    return render(request, "polls/inicio.html", context)

# def filtrarRubros(request):
#     context ={}
 
#     rubro = 

#     titulo = "Rubro"
#     context["dataset"] = Heading.objects.all()
#     context["titulo"] = titulo
         
#     return render(request, "polls/filtrarrubros.html", context)

def filtrarXRubros(request, id):
    context = {}
    rubro = Heading.objects.get(id = id)
    negocios = Business.objects.filter(rubros__id=id)

    context["dataset"] = negocios
    context["rubro"] = rubro

    return render(request, "polls/filtrarrubros.html", context)


