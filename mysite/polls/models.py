from django.db import models
from django.db.models.fields import EmailField


class Client(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cuentaFacebook = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    fechaNacimiento = models.DateTimeField('Fecha de Nacimiento')
    privilegios = models.BooleanField()

    def __str__(self):
        return self.nombre


class Subscription(models.Model):
    nombre = models.CharField(max_length=200)
    precioMensual = models.FloatField()
    caracteristicas = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
     
class Dayweek(models.Model):
    dia = models.CharField(max_length=200)

    def __str__(self):
        return self.dia


class Heading(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class ContactForm(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Business(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fotoNegocio = models.CharField(max_length=200)
    fotoLogotipo = models.CharField(max_length=200)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Businesshourday(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    diaSemana = models.ForeignKey(Dayweek, on_delete=models.CASCADE)
    horaAbre = models.DateTimeField('horario de apertura')
    horaCierra = models.DateTimeField('horario de cierre')

    def __str__(self):
        return self.negocio


class BusinessArea(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    rubro = models.ForeignKey(Heading, on_delete=models.CASCADE)

    def __str__(self):
        return self.negocio



class BusinessContactForm(models.Model):
    formaContacto = models.ForeignKey(ContactForm, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    datosContacto = models.CharField(max_length=200)

    def __str__(self):
        return self.negocio

