
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .urls import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

#from mysite.polls.models import Business
def cargarCliente(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def cargarSuscripcion(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def cargarDiaSemana(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = DayweekForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def cargarRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = HeadingForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)


def cargarFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ContactFormForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

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
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def success(request):
    return HttpResponse('succesfully uploaded')

def cargarNegocioHoraDia(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinesshourdayForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def cargarNegocioRubro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinessAreaForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)

def cargarNegocioFormaContacto(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BusinessContactFormForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "polls/cargar.html", context)







def principal(request):

    return render(request, "polls/inicio.html", {"negocios": Business.objects.all})

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