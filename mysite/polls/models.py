from enum import unique
from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import User


class Client(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default= '')
    # nombre = models.CharField(max_length=200)
    # apellido = models.CharField(max_length=200)
    #cuentaFacebook = models.CharField(max_length=200)
    # email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=200)
    # fechaNacimiento = models.DateField('Fecha de Nacimiento')
    privilegios = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
    
    def getPrivilegios(self):
        privilegiado = ''
        if self.privilegios:
            privilegiado = 'Si'
        else:
            privilegiado = 'No'
        
        return privilegiado



class Subscription(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    precioMensual = models.FloatField()
    caracteristicas = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
     
class Dayweek(models.Model):
    dia = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.dia


class ContactForm(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='images/', verbose_name='logo', default='noneyo')

    def __str__(self):
        return self.nombre

class Heading(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.nombre

class Business(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=200)
    fotoNegocio = models.ImageField(upload_to='images/', verbose_name='Foto del Negocio')
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Subscription, on_delete=models.SET_DEFAULT, default= '')
    rubros = models.ManyToManyField(Heading, through='BusinessArea')
    formasContacto = models.ManyToManyField(ContactForm, through='BusinessContactForm')
    diasSemana = models.ManyToManyField(Dayweek, through='Businesshourday')

    def __str__(self):
        return self.nombre



class Businesshourday(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    diaSemana = models.ForeignKey(Dayweek, on_delete=models.CASCADE)
    horaAbre = models.TimeField(blank=True, null=True, verbose_name='Hora Abre')
    horaCierra = models.TimeField(blank=True, null=True, verbose_name='Hora Cierra')

    def __str__(self):
        return self.negocio.nombre


class BusinessArea(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    rubro = models.ForeignKey(Heading, on_delete=models.CASCADE)

    def __str__(self):
        return self.negocio.nombre



class BusinessContactForm(models.Model):
    formaContacto = models.ForeignKey(ContactForm, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    datosContacto = models.CharField(max_length=200, help_text= 'para número, ingrese el codigo de area seguido del 15 y luego el numero')

    def __str__(self):
        return self.negocio.nombre
    
    def getEnlace(self):
        enlace = ''
        if (self.formaContacto.nombre == 'Facebook'):
            enlace = self.datosContacto
        elif (self.formaContacto.nombre == 'Instagram'):
            enlace = 'https://www.instagram.com/'+self.datosContacto
        elif (self.formaContacto.nombre == 'Llamada'):
            separados = self.datosContacto.split("15", 1)
            separados.insert(0,'+549')
            for item in separados:
                enlace = enlace + item
            enlace = 'tel:'+enlace
        elif (self.formaContacto.nombre == 'WhatsApp'):
            separados = self.datosContacto.split("15", 1)
            separados.insert(0,'549')

            for item in separados:
                enlace = enlace + item
            enlace = 'https://wa.me/'+enlace
        else:
            enlace = 'desconocido'
        return enlace

    def getIcono(self):
        icono = ''
        if (self.formaContacto.nombre == 'Facebook'):
            icono = 'bi bi-facebook'
        elif (self.formaContacto.nombre == 'Instagram'):
            icono = 'bi bi-instagram'
        elif (self.formaContacto.nombre == 'Llamada'):
            icono = 'bi bi-telephone'
        elif (self.formaContacto.nombre == 'WhatsApp'):
            icono = 'bi bi-whatsapp'
        else:
            icono = 'bi bi-exclamation-triangle-fill'
        return icono

    def getColor(self):
        color = ''
        if (self.formaContacto.nombre == 'Facebook'):
            color = 'btn btn-outline-primary'
        elif (self.formaContacto.nombre == 'Instagram'):
            color = 'btn btn-outline-dark'
        elif (self.formaContacto.nombre == 'Llamada'):
            color = 'btn btn-outline-secondary'
        elif (self.formaContacto.nombre == 'WhatsApp'):
            color = 'btn btn-outline-success'
        else:
            color = 'bi bi-exclamation-triangle-fill'
        return color