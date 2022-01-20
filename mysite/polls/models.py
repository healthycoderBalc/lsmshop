from django.db import models
from django.db.models.fields import EmailField


class Client(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cuentaFacebook = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=200)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
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


class ContactForm(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Heading(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Business(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fotoNegocio = models.ImageField(upload_to='images/')
    fotoLogotipo = models.ImageField(upload_to='images/')
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    rubros = models.ManyToManyField(Heading, through='BusinessArea')
    formasContacto = models.ManyToManyField(ContactForm, through='BusinessContactForm')

    def __str__(self):
        return self.nombre



class Businesshourday(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    diaSemana = models.ForeignKey(Dayweek, on_delete=models.CASCADE)
    horaAbre = models.TimeField('horario de apertura')
    horaCierra = models.TimeField('horario de cierre')

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
    datosContacto = models.CharField(max_length=200)

    def __str__(self):
        return self.negocio.nombre

